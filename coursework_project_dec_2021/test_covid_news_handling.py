import unittest
import configparser
import requests
import sched
import time
from covid_news_handling import news_API_request, update_news
from datetime import datetime

current_date = datetime.today().strftime('%Y-%m-%d')

config = configparser.ConfigParser()
config.read('covid_config.cfg')
key = config['VARIABLES']['API_KEY']
print(key)

class TestCovidNewsHandling(unittest.TestCase):
    def test_news_API_request(self):
        news = news_API_request(covid_terms="coronavirus covid-19 covid")
        covid_terms = "coronavirus covid-19 covid"
        url = ('https://newsapi.org/v2/everything?'
           + f'''q={covid_terms}&'''
           + f'''from={current_date}&'''
           + 'sortBy=popularity&'
           + f'''apiKey={key}''')
        response = requests.get(url).json()
        self.assertEqual(news, response)

    def test_update_news(self):
        sched_news = update_news(10, "Test Update", repeat=False)
        scheduler = sched.scheduler(time.time, time.sleep)
        event1 = scheduler.enter(10, 1, news_API_request, kwargs=("Test Update"))
        self.assertEqual(sched_news, event1)

if __name__ == '__main__':
    unittest.main()