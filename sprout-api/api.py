import time
import subprocess
import json

import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
import adafruit_dht

from flask import Flask, Response, jsonify, request

from models import Pump, pHSensor, TDSSensor, WaterLevelSensor
from helpers import *

# Configuration file
with open('config.json', 'r') as f:
    config = json.load(f)

with open('../ports.json', 'r') as f:
    ports = json.load(f)

# Create the SPI bus
spi = busio.SPI(clock = board.SCK, MISO = board.MISO, MOSI = board.MOSI)

# Create the CS (chip select)
cs = digitalio.DigitalInOut(getPin(config['pins']['CS']))

# Create the MCP3008 object
mcp = MCP.MCP3008(spi, cs)

# Defining the sensors
_ph = pHSensor(mcp, config['channels']['PH'])
_tds = TDSSensor(mcp, config['channels']['TDS'])
_waterlevel = WaterLevelSensor(mcp, config['channels']['WATERLEVEL'], config['pins']['WATERLEVEL_POWER'])
dht22 = adafruit_dht.DHT22(getPin(config['pins']['DHT22']), use_pulseio = False)

print(config['pins']['M1'], type(config['pins']['M1']))

# Creating Pump objects
pumps = {   
            1 : Pump(config['pins']['M1']),
            2 : Pump(config['pins']['M2']), 
            3 : Pump(config['pins']['M3']), 
            4 : Pump(config['pins']['M4']), 
            5 : Pump(config['pins']['M5'])
        }

app = Flask(__name__)

# API ENDPOINTS 
@app.route('/temp', methods = ['GET'])
def temperature():

    # While loop is here because communication with DHT tends to fail sometimes.
    while True:
        try: temperature = dht22.temperature
        except RuntimeError: continue
        except Exception: return Response(status = 500)
        else: return jsonify({'temperature': temperature, 'unit': 'C'})
        

@app.route('/humidity', methods = ['GET'])
def humidity():
    
    # While loop is here because communication with DHT tends to fail sometimes.
    while True:
        try: humidity = dht22.humidity
        except RuntimeError: continue
        except Exception: return Response(status = 500)
        else: return jsonify({'humidity': humidity, 'unit': '%'})

@app.route('/ph', methods = ['GET'])
def ph():
    return jsonify({'ph': _ph.value(), 'unit': 'pH'})

@app.route('/tds', methods = ['GET'])
def tds():
    return jsonify({'tds': _tds.value(), 'unit': 'ppm'})

@app.route('/waterlevel', methods = ['GET'])
def waterlevel():
    _waterlevel.switch_on()
    time.sleep(0.3) # Introduce some delay for the sensor to come online
    response = jsonify({'waterlevel': _waterlevel.value(), 'unit': '%'})
    _waterlevel.switch_off()
    return response

@app.route('/pump', methods = ['POST'])
def pump():

    # Extracting parameters from request.
    number = int(request.args['number'])
    action = str(request.args['action']).lower().strip()

    # Tried to access a pump that does not exist.
    if number not in pumps.keys(): 
        return Response(status = 404)
    
    pump = pumps[int(request.args['number'])]

    # Invalid action
    if action not in ['activate', 'deactivate', 'toggle']:
        return Response(status = 405)
    
    _action = getattr(pump, action)
    _action()
    return Response(status = 200)

# This hack uses the command line to get the IPv4 address of the server and then host there
ip = subprocess.getoutput('hostname -I').strip()
app.run(host = ip, port = ports['sprout-api'])