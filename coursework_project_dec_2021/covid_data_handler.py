"""This module has various functions inside it that will allow
    the processing and handling of covid data, whether from a
    CSV file or returned from an API"""
import sched
import time
import logging
import pandas as pd
from typing import List
from uk_covid19 import Cov19API

logging.basicConfig(filename='covid_log.log', level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s %(message)s')

data_list_exeter = []
data_list_england = []


def parse_csv_data(csv_filename: str) -> list:
    """This function will take the csv data from the csv file and return it as a list """
    dataframe = pd.read_csv(csv_filename)
    return dataframe.values.tolist()

# parse_csv_data("nation_2021-10-28.csv")


def process_covid_csv_data(covid_csv_data: object) -> int:
    """This function will take the returned list of data from parse_csv_data()
    (converted to a dataframe here for convenience in accessing values) and will return
    the necessary statistics back to the user """
    covid_csv_data = pd.DataFrame(covid_csv_data)
    num_cases_7_days = int(covid_csv_data[6].head(9).sum(axis=0, skipna=True) -
                           covid_csv_data._get_value(1, 6, takeable=True))
    current_num_hosp_cases = int(covid_csv_data._get_value(0, 5, takeable=True))
    cum_num_deaths = int(covid_csv_data._get_value(13, 4, takeable=True))

    return num_cases_7_days, current_num_hosp_cases, cum_num_deaths

# process_covid_csv_data(covid_csv_data=parse_csv_data("nation_2021-10-28.csv"))


def covid_API_request(location: str, location_type: str) -> List[dict]:
    """This function will use the Cov19API provided by
    Public Health England and return all of the values of the given
    fields, from the start date up to the current date. This data
    is returned in a JSON format."""
    location_data = [
        'areaType='+str(location_type),
        'areaName='+str(location)
    ]
    covid_data = {
        "date": "date",
        "areaName": "areaName",
        "areaCode": "areaCode",
        "newCasesByPublishDate": "newCasesByPublishDate",
        "cumCasesByPublishDate": "cumCasesByPublishDate",
        "hospitalCases": "hospitalCases",
        "newDeaths28DaysByDeathDate": "newDeaths28DaysByDeathDate",
        "cumDeaths28DaysByDeathDate": "cumDeaths28DaysByDeathDate",
        "cumDeathsByPublishDate": "cumDeathsByPublishDate"
    }

    api_object = Cov19API(filters=location_data, structure=covid_data)
    data = api_object.get_json()
    return data

# covid_API_request()

exe = covid_API_request(location="Exeter", location_type="ltla")
eng = covid_API_request(location="England", location_type="nation")
for piece in exe['data']:
    data_list_exeter.append(piece)
for info in eng['data']:
    data_list_england.append(info)

df_exeter = pd.DataFrame(data_list_exeter)
df_england = pd.DataFrame(data_list_england)

# print(data_list_england)

national_7day_infections = int(df_england['newCasesByPublishDate'].head(7).sum(axis=0, skipna=True))
local_7day_infections = int(df_exeter['newCasesByPublishDate'].head(7).sum(axis=0, skipna=True))
# print(national_7day_infections)
# print(local_7day_infections)

scheduler = sched.scheduler(time.time, time.sleep)

def schedule_covid_updates(update_interval: int, update_name: str, repeat=False) -> List[object]:
    """This function allows the user to schedule updates
    for when they want the Cov19API to get values at."""
    if not repeat:
        event1 = scheduler.enter(update_interval, 1, covid_API_request, kwargs=update_name)
        logging.info(f"""Covid update for {update_name} has been scheduled""")
        return event1
    if repeat:
        for i in range(100000):
            rep = 0
            event2 = scheduler.enter(update_interval + rep, 2, covid_API_request,
                                 argument=repeat, kwargs=update_name)
            rep += 86400
            i += 1
        logging.info(f"""Repeating covid update for update {update_name}""")
        return event2
    scheduler.run(blocking=False)
