import logging
import time
import os
import libhoney

from dotenv import load_dotenv
load_dotenv()

trigger_url = os.environ.get("TRIGGER_URL")
honeycomb_api_key = os.environ.get("HONEYCOMB_API_KEY")
libhoney.init(writekey=honeycomb_api_key, dataset="pir-trigger", debug=True, block_on_send=True)

# Write pid to file so we can kill it if needed
f = open("pid.txt", "w")
f.write(str(os.getpid()))
f.close()

# Function to send Honeycomb Telemetry event
def send_telemetry(timeout = True, webhook_satus_code = 0):
    ev = libhoney.new_event()
    ev.add({
        "webhook_status_code": webhook_satus_code,
        "timeout": timeout
    })
    ev.send()

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
        send_telemetry(False, res.status_code)
        print("Trigger request response ", res.status_code)
    else:
        print("Motion detected (inside timeout)")
        send_telemetry
    motion_time = time.time()
    pir.wait_for_no_motion()

