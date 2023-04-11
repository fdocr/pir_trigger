import logging
import time
import os

from dotenv import load_dotenv
load_dotenv()
trigger_url = os.environ.get("TRIGGER_URL")

# Write pid to file so we can kill it if needed
f = open("pid.txt", "w")
f.write(str(os.getpid()))
f.close()

import requests
from gpiozero import MotionSensor
pir = MotionSensor(4)
timeout = 45
motion_time = time.time() - timeout

while True:
    pir.wait_for_motion()
    if (time.time() - motion_time) > timeout:
        print("Motion detected")
        res = requests.get(trigger_url)
        print("Trigger request response ", res.status_code)
    else:
        print("Motion detected (inside timeout)")
    motion_time = time.time()
    pir.wait_for_no_motion()

