from functions import *
from datetime import datetime

# https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/120.0.6099.109/win32/chromedriver-win32.zip
# Selenium chrome driver
userTime = getUserTime()

# Gets current time, converts to string of Hours:Minutes format
currentTime = datetime.now().time()
currentTime = currentTime.strftime("%H:%M")

while currentTime != userTime:
    # Check if current time is equal to time set by user every 30 sec
    time.sleep(30)

    # Converts current time to string of Hours:Minutes format
    currentTime = datetime.now().time()
    currentTime = currentTime.strftime("%H:%M")

# Emails used for booking
emails = ["jasonwang9", "durvishanthananchaya", "patrickwu4", "huzaifarehan"]
# bookAllRooms(emails)
print("Running script")
