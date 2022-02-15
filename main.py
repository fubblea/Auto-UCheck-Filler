from splinter import Browser
import os
import dotenv

browser = Browser(driver_name="chrome")

browser.visit('https://ucheck.utoronto.ca')

# Login
dotenv.load_dotenv()
browser.find_by_name("j_username").fill(os.getenv("USER"))
browser.find_by_name("j_password").fill(os.getenv("PASS"))
browser.find_by_name("_eventId_proceed").click()