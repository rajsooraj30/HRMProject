from datetime import datetime
import os
from pathlib import Path

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
BaseUrl="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
user_name="Admin"
password="admin123"

@pytest.fixture(scope="class",autouse=True)
def browser_setup(request):
    chromeOptions=Options()
    chromeOptions.add_experimental_option("detach",True)
    request.cls.driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()) , options=chromeOptions)

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    today= datetime.now()
    report_dir= Path("hrmreports", "Reports_"+today.strftime("%y%m%d"))
    report_dir.mkdir(parents=True,exist_ok=True)
    report_file = report_dir / f"Report_{today.strftime('%y%m%d%H%M')}.html"
    config.option.htmlpath=report_file
    config.option.self_contained_html =True

def pytest_html_report_title(report):
    report.title ="HRM Test Report"