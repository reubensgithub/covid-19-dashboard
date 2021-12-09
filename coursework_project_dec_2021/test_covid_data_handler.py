import unittest
import sched
import time
from uk_covid19 import Cov19API
from covid_data_handler import parse_csv_data, process_covid_csv_data, covid_API_request, schedule_covid_updates


class TestCovidDataHandler(unittest.TestCase):
    def test_parse_csv_data(self):
        parse = parse_csv_data("nation_2021-10-28.csv")
        self.assertEqual(len(parse), 638)

    def test_process_covid_csv_data(self):
        process = process_covid_csv_data(covid_csv_data=parse_csv_data("nation_2021-10-28.csv"))
        self.assertEqual(process, (240299, 7019, 141544))

    def test_covid_API_request(self):
        request = covid_API_request(location="Exeter", location_type="ltla")
        location_data = [
            'areaName=Exeter',
            'areaType=ltla'
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
        self.assertEqual(request, data)

    def test_schedule_covid_updates(self):
        sched_cov = schedule_covid_updates(10, "Test Update", repeat=False)
        scheduler = sched.scheduler(time.time, time.sleep)
        event1 = scheduler.enter(10, 1, covid_API_request, kwargs=("Test Update"))
        self.assertEqual(sched_cov, event1)

if __name__ == '__main__':
    unittest.main()