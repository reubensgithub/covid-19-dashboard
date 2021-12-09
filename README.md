# README file for the COVID-19 Dashboard


![Project Image](https://phil.cdc.gov//PHIL_Images/23311/23311_lores.jpg)
---

### Table of Contents:

- [Description](#description)
- [Installation](#references)
- [Getting Started](#getting-started)
- [How to use](#how-to-use)
- [Testing](#testing)
- [License](#license)
- [Author Info](#author-info)

---

## Description

The program I have created is a COVID-19 Dashboard, which, when run, will display a clean, simple UI
that displays the current COVID data, along with news articles related to COVID-19 and a 'schedule updates' feature.


#### Technologies

- Covid-19 API
- News API

[Back To The Top](#)

---

##### Covid 19 API
- The Covid 19 API, supplied by Public Health England, is what is used in my program to fetch live and up-to-date COVID-19 data when the user schedules an update to do so.


##### News API
- The News API, supplied by NewsAPI, is what is used in my program to fetch recently published articles related to COVID-19/Coronavirus.

---

## Getting started:

To get started, you'll need to meet the following pre-requisites:
- Python 3.8 (the program was developed on a system that utilised Python 3.8.10)
- pip (or conda) installer (we will be using pip or conda to install the modules required, however this should come pre-installed when you download Python)
- The uk-covid19 module installed \
Link to install: https://publichealthengland.github.io/coronavirus-dashboard-api-python-sdk/pages/getting_started.html)
- The flask module (the program was developed on a system that utilised Flask 1.1.2) \
Link to install: https://flask.palletsprojects.com/en/2.0.x/installation/#install-flask)
- The pandas module

[Back To The Top](#)

### Installing the uk-covid19 module
```html
pip install uk-covid19
```
To install the uk-covid19 module, copy the above line and paste it into command prompt on your device, then hit enter.
NOTE: For certain IDEs, like PyCharm, you'll have to install the module within the IDE as well.
[Back To The Top](#)


### Installing flask
```html
pip install flask
```
To install the flask module, copy the above line and paste it into command prompt on your device, then hit enter.
NOTE: For certain IDEs, like PyCharm, you'll have to install the module within the IDE as well.
[Back To The Top](#)

### Installing pandas
```html
pip install pandas
```
To install the pandas module, copy the above line and paste it into command prompt on your device, then hit enter.
NOTE: For certain IDEs, like PyCharm, you'll have to install the module within the IDE as well.
[Back To The Top](#)

---

## How to Use
```html
python3 user_interface.py
```
To use the program, run Python on command prompt or use python IDLE / an IDE.
Once python has started running, open the user_interface.py file and run that file.
Then, click on the link given (it should look something like: 127.0.0.1/5000) \
[Back To The Top](#)
---
## Testing
Testing is essential as it makes sure all of the modules are working as they should.
There are two test files. One is called test_covid_data_handler.py , which as suggested by its name, test to see if the covid_data_handler module is working as it should
The second test file is called test_covid_news_handling.py, which will test the covid_news_handling file works as it should.

```html
python3 test_covid_data_handler.py
```

Should the tests fail, please contact me via the contact details below.
[Back To The Top](#)
---
## License

MIT License

Copyright (c) [2021] [Reuben Kurian]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---
## Author Info

- Email - [Reuben Kurian](rk509@exeter.ac.uk)

[Back To The Top](#)
