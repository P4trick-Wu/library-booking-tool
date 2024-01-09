from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win32/chromedriver-win32.zip
# Selenium chrome driver

# Set up chrome driver and open chrome, prevents cannot read tbsCertificate issue
options = webdriver.ChromeOptions()

options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(
    service=Service("chromedriver.exe"),
    options=options,
)

# Navigates to the ealiest possible booking date for room 234C
driver.get("https://carletonu.libcal.com/space/26977")
element = driver.find_element(By.CLASS_NAME, "fc-next-button")
for i in range(7):
    element.click()

# Stores all timeslots in an array
elements = WebDriverWait(driver, 10).until(
    # waits until all timeline slots have loaded in
    EC.presence_of_all_elements_located((By.CLASS_NAME, "fc-timeline-event-harness"))
)

# Accesses 6:30 pm timeslot
elements[-7].click()
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "input-group"))
)
element.click()

# Chooses selection box option and clicks on the last option
options = element.find_elements(By.TAG_NAME, "option")
# options[-1].click()
# change index to -1 on final version, only selects 30 minutes for now
options[0].click()

# Submits the time slot and length selected
submit = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "submit_times"))
)
submit.click()

# Clicks button to accept library terms & conditions
submitTerms = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "terms_accept"))
)
submitTerms.click()

# Types first name into text box
firstNameBox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "fname"))
)
firstNameBox.send_keys("Patrick")

# Types last name into text box
lastNameBox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "lname"))
)
lastNameBox.send_keys("Wu")

# Types email into text box
emailBox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "email"))
)
emailBox.send_keys("patrickwu4@cmail.carleton.ca")

# Final submit, completes booking
# finalSubmit = WebDriverWait(driver, 10).until (
#     EC.presence_of_element_located((By.ID, "btn-form-submit"))
# )
# finalSubmit.click()

# Exits the tab
time.sleep(10)

driver.quit()
