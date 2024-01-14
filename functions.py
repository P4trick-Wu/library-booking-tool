from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date, timedelta
import time


# Books all the rooms using emails provided in emailList
def bookAllRooms(emailList):
    print("Booking rooms")

    # Set up chrome driver and open chrome, prevents cannot read tbsCertificate issue
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(
        service=Service("chromedriver.exe"),
        options=options,
    )

    # Books all rooms

    # bookRoom(driver, "patrickwu4@cmail.carleton.ca", "Patrick", "Wu", 8)
    # bookRoom(driver, "patrickwu4@cmail.carleton.ca", "Patrick", "Wu", 9)
    # bookRoom(driver, "patrickwu4@cmail.carleton.ca", "Patrick", "Wu", 10)

    # Books from 8:30am to 8:30pm

    bookRoom(driver, "jasonwang9@cmail.carleton.ca", "Jason", "Wang", 1)

    bookRoom(driver, "patrickwu4@cmail.carleton.ca", "Patrick", "Wu", 7)

    bookRoom(
        driver,
        "durvishanthananchaya@cmail.carleton.ca",
        "Durvishan",
        "Thananchayan",
        13,
    )
    bookRoom(driver, "huzaifarehan@cmail.carleton.ca", "Huzaifa", "Rehan", 19)

    # Send info to Jason's website
    sendWebsiteInfo(driver)

    time.sleep(10)
    driver.quit()


def sendWebsiteInfo(driver):
    print("Sending info to Jason's website:")

    driver.get("https://bookings.jasonwangg.me/")

    # Sends name of the room
    roomName = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "roomName"))
    )
    roomName.send_keys("234C")

    # Sends booking date
    dateBox = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "date"))
    )

    # Gets current date and adds 7 days
    bookingDate = date.today()
    bookingDate += timedelta(days=7)

    dateBox.send_keys(str(bookingDate))

    # Submits data
    submitButton = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "button"))
    )
    submitButton.click()


# Books one room for maximum time (up to 3 hours) using a single email
def bookRoom(driver, email, fName, lName, slotNum):
    print("Booking a room")

    findDate(driver)

    # Accesses time slot, accept terms and fill in necessary info
    timeSlots = getTimeSlots(driver)
    timeSlots[slotNum].click()

    selectTime(driver)

    fillInfo(driver, email, fName, lName)

    # Final submit to complete booking
    finalSubmit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "btn-form-submit"))
    )
    finalSubmit.click()

    time.sleep(1)

    print(" Final submit complete")


# Fills in first name, last name and email into form
def fillInfo(driver, email, fName, lName):
    print(" Filling information")

    # Types first name into text box
    firstNameBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "fname"))
    )
    firstNameBox.send_keys(fName)

    # Types last name into text box
    lastNameBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "lname"))
    )
    lastNameBox.send_keys(lName)

    # Types email into text box
    emailBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    emailBox.send_keys(email)


# Clicks on longest available booking length in selection box, then submits
def selectTime(driver):
    selectionBox = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "input-group"))
    )
    selectionBox.click()

    # Stores length of booking time in array, clicks on longest time
    timeLengths = selectionBox.find_elements(By.TAG_NAME, "option")

    # Timelengths index should be set to -1 for longest possible time
    timeLengths[-1].click()
    # timeLengths[0].click()

    # Submits time slot and length selected
    submit = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "submit_times"))
    )
    submit.click()

    # Accepts library terms & conditions
    submitTerms = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "terms_accept"))
    )
    submitTerms.click()


# Navigates to the earliest possible booking date for room 234C
def findDate(driver):
    driver.get("https://carletonu.libcal.com/space/26977")
    element = driver.find_element(By.CLASS_NAME, "fc-next-button")

    # Change number in for loop to 7 when in proper use
    for i in range(7):
        element.click()


# returns all timeslots stored in an array
def getTimeSlots(driver):
    elements = WebDriverWait(driver, 10).until(
        # waits until all timeline slots have loaded in
        EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "fc-timeline-event-harness")
        )
    )

    return elements

# returns the time the user wants to execute the program

def getUserTime():
    userTime = input("Enter time in 24 hour format (HH:MM): ")
    return userTime
