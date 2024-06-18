import requests
from ddt import data
from testpage import OperationsHelper
from selenium import webdriver
import logging
import yaml
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    name = testdata["username"]
    passwd = testdata["password"]


def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(name)
    testpage.enter_pass(passwd)
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {name}"


def test_step3(browser):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.click_about_btn()
    assert testpage.check_font_size(), "Expected font size to be 32px, but it's not."