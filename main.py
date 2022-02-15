import os
import time

import dotenv
from splinter import Browser, exceptions

browser = Browser(driver_name="chrome")

browser.visit('https://ucheck.utoronto.ca')

# Login
dotenv.load_dotenv()
browser.find_by_name("j_username").fill(os.getenv("USER"))
browser.find_by_name("j_password").fill(os.getenv("PASS"))
browser.find_by_name("_eventId_proceed").click()

try:
    browser.find_by_text("Start health screening questionnaire", wait_time=5).click()
except exceptions.ElementDoesNotExist:
    browser.find_by_text("New Self-Assessment", wait_time=5).click()

browser.find_by_text("Yes", wait_time=5).click()
time.sleep(0.5)

i=1
while i <= 6:
    browser.find_by_text("No", wait_time=5)[i].click()
    i+=1
    time.sleep(0.5)

browser.find_by_text("Submit", wait_time=5).click()