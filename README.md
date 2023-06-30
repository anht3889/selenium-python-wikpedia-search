# Automation Project

This is the sample project used to test API and UI for Search functionality of Wikipedia.
- Selenium framework is used for UI test
- requests lib is used for API test
- I'm using pytest framework and allure for report

## Project Structure
- [api](api) - this is used for api test functions
- [base](base) - this is base page which contains common functions
- [data](data) - this directory contains test data
- [helpers](helpers) - the listener which logs for each action of web driver
- [locators](locators) - where to store all locators separately
- [pages](pages) - there are sets of method for each test step
- [reports](reports) - if you run tests with Allure, tests reports will be saved in this directory
- [tests](tests) - there are sets of tests for main functionalities of website
- [utils](utils) - this directory contains files responsible for configuration, e.g. [driver_factory.py](utils/driver_factory.py) for webdriver management or [read_csv.py](utils/read_csv.py) for reading input data from csv files included in project

## Install Required Libs
Run the command below in terminal:

```
$ pip install -r requirements.txt
```

Install Allure to view reports as following instruction: https://docs.qameta.io/allure/#_installing_a_commandline

## Run Automated Tests and Generate Reports

To generate all tests report using Allure you need to run tests by command first:
```
$ pytest --alluredir=<reports directory path>
```
After that you need to use command to view reports:
```
$ allure serve <reports directory path>
```