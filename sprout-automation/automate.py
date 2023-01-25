import requests
import json
import subprocess
import time

from tasks import Task

# Load config files
with open('../ports.json', 'r') as f:
    ports = json.load(f)

with open('../pumps.json', 'r') as f:
    pumps = json.load(f)

# This function is called after every interval.
def automate():
    try:
        # Get API URL
        apiURL = 'http://' + subprocess.getoutput('hostname -I').strip() + f":{ports['sprout-api']}"
        
        # Actuate pumps if needed -- should probably take the mean of 5-10 readings though
        with requests.get(f'{apiURL}/tds') as r:
            if r.json()['tds'] < 500:
                requests.post(f'{apiURL}/pump?number={pumps["nutrients"]}&action=activate')
                time.sleep(2)
                requests.post(f'{apiURL}/pump?number={pumps["nutrients"]}&action=deactivate')
        
        with requests.get(f'{apiURL}/waterlevel') as r:
            if r.json()['waterlevel'] < 10:
                requests.post(f'{apiURL}/pump?number={pumps["nutrients"]}&action=activate')
                requests.post(f'{apiURL}/pump?number={pumps["water"]}&action=activate')
                time.sleep(2)
                requests.post(f'{apiURL}/pump?number={pumps["nutrients"]}&action=deactivate')
                requests.post(f'{apiURL}/pump?number={pumps["water"]}&action=deactivate')

    except Exception as e:
        print(f'{type(e).__name__}: {e}')

# Create and start task
automate_task = Task(task = automate, sleep = 60)
automate_task.start()