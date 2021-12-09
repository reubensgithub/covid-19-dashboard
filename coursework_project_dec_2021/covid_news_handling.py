"""This module's purpose is to return the news
    articles related to covid and to be able to
    schedule regular updates for when the user wants
    the displayed news articles to update"""
import logging
import configparser
import sched
import time
from datetime import datetime
import requests
from newsapi import NewsApiClient
from typing import List

current_date = datetime.today().strftime('%Y-%m-%d')

config = configparser.ConfigParser()
config.read('covid_config.cfg')

logging.basicConfig(filename='covid_log.log', level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s %(message)s')

articles_list = []
title_list = []

def news_API_request(covid_terms: str) -> List[dict]:
    """This function will use the NewsApi to get news articles
        related to covid from the internet and return them as a
        list."""
    key = config['VARIABLES']['API_KEY']
    newsapi = NewsApiClient(api_key=key)
    covid_headlines = newsapi.get_top_headlines(
        q="Covid" or "covid" or "COVID" or "covid-19" or "Covid-19" or
          "COVID-19" or "coronavirus" or "CORONAVIRUS" or "Coronavirus",
        language='en', country='gb')
    url = ('https://newsapi.org/v2/everything?'
           + f'''q={covid_terms}&'''
           + f'''from={current_date}&'''
           + 'sortBy=popularity&'
           + f'''apiKey={key}''')
    response = requests.get(url).json()
    for item in response['articles']:
        articles_list.append(item)
    return response

news_API_request(covid_terms="coronavirus covid-19 covid")

for article in articles_list:
    title_list.append(article['title'])

scheduler = sched.scheduler(time.time, time.sleep)

def update_news(update_interval: int, update_name: str, repeat=False) -> List[object]:
    """This function allows the user to schedule updates
        for when they want the NewsApi to get new news
         articles at."""
    if not repeat:
        event1 = scheduler.enter(update_interval, 1, news_API_request, kwargs=(update_name))
        logging.info(f"""News update for {update_name} has been scheduled""")
        return event1
    if repeat:
        for i in range(100000):
            rep = 0
            event2 = scheduler.enter(update_interval + rep, 2, news_API_request,
                                     argument=repeat, kwargs=update_name)
            rep += 86400
            i += 1
        logging.info(f"""Repeating news update for update {update_name}""")
        return event2
    scheduler.run(blocking=False)
