<img display="block" margin-left="auto" margin-right="auto" width="50%" alt="Screenshot 2023-01-25 at 7 50 57 PM" src="https://user-images.githubusercontent.com/77115883/214588540-53785370-f6b8-4078-9ff4-59791c1c5ea9.png">


# Table of Contents

* [Background](#background)
* [Objective](#objective)
* [Scope](#scope)
* [Literature Survey](#literature-survey)
* [Project Design](#project-design)
* [System Architecture](#system-architecture)
* [Languages](#Languages)
* [Circuit Diagram](#circuit-diagram)
* [Conclusion](#conclusion)


## Background

Home gardens grant access to cheaper, fresher and more sustainable produce. Owning a home garden is one of the simplest things that one can do to move towards self-sufficiency and reducing the load on the environment. Besides this, one can control what fertilizers and pesticides go into the plant. Apart from this, it adds to the aesthetic value and provides a positive environment at home. However, in today’s world, people live busy lives. They have many different tasks to focus on, like their jobs, education, and side projects. Most people do not have the time or resources available to make or maintain a home garden.
Hydroponics is the study of growing plants in a liquid nutrient medium, without the need for soil. The roots of the plant are immersed in the nutrient solution, and the plants receive their nourishment from there.

## Objective

To design and build a system that automates the process of monitoring the plant’s health and watering/fertilizing it. The relevant information about the nutrient levels, pH, humidity and temperature should also be available to the user.

## Scope

- This project specifically targets hydroponic farming. The reason for this is that hydroponic farms are more cost effective and easier to control with the help of pumps.
- This product only targets the people living in urban or suburban areas, who want to have an indoor farm without the hassle of having to maintain it.
- Although the target audience is limited, even actual hydroponic farmers working on larger scales may make use of this system by scaling it up.
- This project is intended to be a prototype and a proof of concept.
- A successful prototype would be one that would be able to fully regulate the nutrient concentration by making use of pumps. It should also be able to report the current nutrient concentration in the medium, along with the current pH and temperature through a webpage.
- While this project is intended to be as energy efficient as possible, there will be no special provisions for powering it using renewable energy. It will be powered directly through a standard 220V power outlet.



## Literature Survey

The Kratky Method is detailed in [1], which is a research paper written by B. A. Kratky. In the Kratky Method, the plant’s roots are immersed in a nutrient solution.
We also used the internet to search for similar projects that had been done before. [2] describes a similar project that was built using the ESP8266 board and an ATMega microcontroller. It made use of a pH sensor and a DHT11 temperature sensor, along with an ultrasonic sensor to detect water level. It makes use of a Mobile app to deliver the data to the user.
[3] describes another project, which was made using 3 Arduino boards and a Raspberry Pi to act as a web server. Two Arduinos act as “Nodes”, which serve to get data from the sensors and send the data to a third Arduino using a radio signal. The third Arduino acts as a gateway, and sends this data to the Raspberry Pi which acts as a web server, running a monitoring and control program. The system delivers data through an Android app. Upon comparison, the plants were shown to grow better indoors while using this system, as compared to the same plant growing outdoors.
[4] explores a similar system, making use of a NodeMCU ESP8266. This board publishes sensor data to a Raspberry Pi 3 Model B using the MQTT protocol, which is a protocol used for IoT devices to communicate with each other. The Raspberry Pi communicates with a Node Red server, which is used for automation purposes and also serves to deliver the sensor data to the user.
After learning what hydroponics is, and exploring the Kratky Method of hydroponics, looking at the different approaches that may be used to create a system to manage a hydroponic system, we may proceed onto the next step.


## Project Design

After reviewing the different approaches in the literature survey stage, we decided to use a
Raspberry Pi as the main component of the system. The system would feature 4 sensors, a TDS sensor, a pH sensor, a temperature and humidity sensor, and a water level sensor.
Apart from this, the Raspberry Pi would also be connected to pumps, which would be able to pump water or nutrients into the solution, or pump the solution out if needed.
The Raspberry Pi would monitor the sensor data, and upon noticing a deviation from the expected nutrient concentration value or the expected pH value, it would trigger the pumps and correct it.
The Raspberry Pi should also be able to provide the sensor data onto a webpage, from where the sensor values can be read by the user.
The project would use Python and Flask for the backend, while HTML, CSS and JS would be appropriate for the frontend.

## Sensors

- Temperature and Humidity Sensor: DHT22
- pH Sensor: KPE-03 probe + pH-4502C module
- TDS Sensor: DFRobotics TDS Meter v1.0
- Water Level Sensor: Funduino Water Level Sensor


## System Architecture

<img width="998" alt="Screenshot 2023-01-25 at 8 05 46 PM" src="https://user-images.githubusercontent.com/77115883/214591432-d714a790-7aba-4dda-afe2-7b3f5a10cfd0.png">


