from functions import *
import datetime


# https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win32/chromedriver-win32.zip
# Selenium chrome driver
userTime = getUserTime()

# converts string userTime to time object
targetTime = datetime.datetime.strptime(userTime, "%H:%M").time()

currentTime = datetime.datetime.now().time()

while currentTime < targetTime:
    time.sleep(30)  # Check every 30 seconds
    # now = datetime.datetime.now().time()
    currentTime = datetime.datetime.now().time()

# Emails used for booking
emails = ["jasonwang9", "durvishanthananchaya", "patrickwu4", "huzaifarehan"]
bookAllRooms(emails)
