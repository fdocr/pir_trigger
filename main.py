import logging
import time
from dotenv import load_dotenv
load_dotenv()

import os
trigger_url = os.environ.get("TRIGGER_URL")

import requests
from gpiozero import MotionSensor
pir = MotionSensor(4)
timeout = 20
motion_time = time.time() - timeout

while True:
    pir.wait_for_motion()
    if (time.time() - motion_time) > timeout:
        print("Motion detected")
        res = requests.get(trigger_url)
        print("Trigger request response ", res.status_code)
    motion_time = time.time()
    pir.wait_for_no_motion()

