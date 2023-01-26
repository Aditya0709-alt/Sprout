<img margin-left="60%" width="350" alt="Screenshot 2023-01-25 at 7 50 57 PM" src="https://user-images.githubusercontent.com/77115883/214588540-53785370-f6b8-4078-9ff4-59791c1c5ea9.png">


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

## Flow Diagram

<img width="691" alt="Screenshot 2023-01-25 at 8 06 52 PM" src="https://user-images.githubusercontent.com/77115883/214591714-68937195-3032-4132-9717-f6992e390a23.png">


## Languages

- Python
- HTML/CSS
- Javascript

## Circuit Diagram

<img width="707" alt="Screenshot 2023-01-25 at 8 08 49 PM" src="https://user-images.githubusercontent.com/77115883/214592129-fb991a7a-b8de-4c8d-a584-a9a1c09200b2.png">


## PCB

The major problem with the breadboard was that it involved using a lot of wires. This made it complex to assemble, and also very difficult to carry. It did not look appealing or presentable. Also, the breadboard connections are somewhat loose, due to which there would be chances of components getting unplugged during operation. This could cause damage to the components.


<img width="795" alt="Screenshot 2023-01-25 at 8 09 18 PM" src="https://user-images.githubusercontent.com/77115883/214592241-0f23fe02-fdf5-45c6-8ede-c747a3a476ec.png">


## Features

- Read sensor data and provide it over an API.
- Read sensor data and provide it on the webpage.
- If the nutrient content is low, it can actuate the pumps to deliver nutrients to the plant. If the water level is low, it can actuate the pumps to deliver water to the plant.
- It also has one pump designated to drain the plant tank.
- There are a total of 5 pumps, of which two are currently not used. However, they may be incorporated into the system to pump solutions to increase or decrease the pH of the solution.


![PHOTO-2022-05-13-12-21-33](https://user-images.githubusercontent.com/77115883/214760079-4f281de0-74fe-4a1e-b36e-cb64a59074f1.jpg)

![IMG_1493](https://user-images.githubusercontent.com/77115883/214760503-8da83df8-ab87-44c6-bb3d-20e648264f7a.jpg)

![IMG_1494](https://user-images.githubusercontent.com/77115883/214760545-974d4cff-8046-49b7-90f1-a9cde79617ad.jpg)


## Conclusion

The final product obtained was a product that was capable of maintaining a hydroponic garden on its own for a very long time. As long as the reservoirs are full and the system is connected to power, it will continue to function. Overall, the results were satisfactory and aesthetically pleasing. However, a much longer testing period is required to gain insight into the efficiency and effectiveness of the system.


## Future Scope

- There is still room for improvement in this project. An actual, 3D printed enclosure for both
the circuits and a custom 3D printed planter to hold the sensors in place would benefit the system a lot.
- The system may be improved by adding data storage capabilities to it. So, the sensors would be able to record data, and the user can gain access to the raw data or plot graphs using it.
- The accuracy of the sensors may be improved by further calibration.
- Lastly, it would be very interesting to incorporate machine learning or artificial intelligence into this project. A machine learning algorithm could monitor the plants behaviours and make predictions about it. A camera could be connected to the plant, and the machine learning algorithm would be able to detect plant diseases or other deficiencies and notify the user before they have a chance to hurt the growth of the plant.




## References

[1] Kratky, B. A. (2009). Three non-circulating hydroponic methods for growing lettuce. Acta Horticulturae, (843), 65–72. https://doi.org/10.17660/actahortic.2009.843.6
[2] Dr. Asawari Dudwadkar. (2020). Automated hydroponics with remote monitoring and control using IOT. International Journal of Engineering Research And, V9(06). https://doi.org/10.17577/ijertv9is060677
[3] Palande, V., Zaheer, A., & George, K. (2018). Fully Automated Hydroponic System for Indoor Plant Growth. Procedia Computer Science, 129, 482–488. https://doi.org/10.1016/j.procs.2018.03.028
[4] Lakshmanan, R., Djama, M., Perumal, S., & Abdulla, R. (2020). Automated smart hydroponics system using the internet of things. International Journal of Electrical and Computer Engineering (IJECE), 10(6), 6389. https://doi.org/10.11591/ijece.v10i6.pp6389-6398
Department of Computer Engineering (MP Jan-Apr 2022) Page 21



