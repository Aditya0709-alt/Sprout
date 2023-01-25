import requests
import subprocess
import time
import json
import os

from flask import Flask, Response, jsonify, render_template
app = Flask(__name__)

with open('../ports.json', 'r') as f:
    ports = json.load(f)

with open('../pumps.json', 'r') as f:
    pumps = json.load(f)

ip = subprocess.getoutput('hostname -I').strip()
apiPort = ports['sprout-api']
appPort = ports['sprout']
apiURL = f'http://{ip}:{apiPort}'

@app.route('/')
def home():

    try:
        # Create empty dict
        data = dict()

        # Get sensor data one by one
        with requests.get(f'{apiURL}/temp') as r:
            data['temperature'] = r.json()['temperature']
        
        with requests.get(f'{apiURL}/humidity') as r:
            data['humidity'] = r.json()['humidity']

        data['tds'] = 0
        data['ph'] = 0
        data['waterlevel'] = 0

        # Taking the mean of 10 readings for Analog Sensors
        for i in range(10):
            with requests.get(f'{apiURL}/tds') as r:
                data['tds'] += r.json()['tds']/10
            
            with requests.get(f'{apiURL}/ph') as r:
                data['ph'] += r.json()['ph']/10

            with requests.get(f'{apiURL}/waterlevel') as r:
                data['waterlevel'] += r.json()['waterlevel']/10

        return render_template('index.html', data = data)

    except Exception as e:
        return jsonify({'error': f'{type(e).__name__}: {e}'}), 500
        

@app.route('/emptytank', methods = ['POST'])
def emptytank():
    try:
        requests.post(f'{apiURL}/pump?number={pumps["drain"]}&action=activate')
        time.sleep(10)
        requests.post(f'{apiURL}/pump?number={pumps["drain"]}&action=deactivate')
        return Response(status = 200)

    except Exception as e:
        return jsonify({'error': f'{type(e).__name__}: {e}'}), 500
    

if __name__ == '__main__':
    app.run(host = ip, port = appPort)