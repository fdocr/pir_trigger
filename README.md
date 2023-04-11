# PIR Trigger

Script that connects a [PIR Sensor](https://projects.raspberrypi.org/en/projects/physical-computing/11) to a webhook.

# Usage

Clone the repo in a folder, install dependencies and then run in background

```bash
# Install requirements
pip install -r requirements.txt

# Run in background
# TODO: Find/Document a better way to do this
TRIGGER_URL="<webhook_url>" python main.py &
```

Otherwise add `TRIGGER_URL = "<webhook_url>"` to an `.env` file and the script will pick it up
