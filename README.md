# PIR Trigger

Script that connects a PIR Sensor to a webhook.

# Usage

Clone the repo in a folder, install dependencies and then run in background

```bash
# Install requirements
pip install -r requirements.txt

# Run in background
# TODO: Find/Document a better way to do this
TRIGGER_URL="<webhook_url>" python main.py &
```

Otherwise add `TRIGGER_URL = "<webhook_url>"` to an `.env` file and the script will pick it up.

The script writes its own PID to `pid.txt` so it can be used. Examples:

```bash
# Follow output of background process
tail -f /proc/$(cat pid.txt)/fd/1

# Kill process
kill -9 $(cat pid.txt)
```

# Sensor to board connections

[Cable diagram here](https://projects-static.raspberrypi.org/projects/physical-computing/248971027a596f3437da45bafd2bd8a8cc35cb95/en/images/pir_wiring.png)

The script was inspired by [this Raspberry Pi Foundation article](https://projects.raspberrypi.org/en/projects/physical-computing/11) and uses their suggested example layout. The sensor needs 5v (Vcc) and Ground (Gnd), so PIN 2 and PIN 6 work well. Connect the sensor's output (Out) to PIN 7 (GPIO 4).