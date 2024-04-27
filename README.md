# LDWS
Lane departure warning system using python and opencv, Lane departure and collision warning system is an important aspect of ADAS feature. We have focused on making
a prototype and a real-life implementation. ADAS features such as lane departure warning and collision warning
system are tested on the prototype car which consists of detection of lanes through camera and an algorithm for
departure warning. Collision warning is detected using ultrasonic and IR sensors mounted on the prototype car on
the required locations, and the camera video is captured and processed on a Raspberry-Pi-4 B board . The lane
departure warning system is made using opencv and deep learning techniques where the lane markings are detected
and a departure warning is issued whenever the prototype crosses the lane. Similarly collision warning is raised
whenever the obstacle is near towards the moving prototype. It gives early warning hence making the user alert
about the obstacle it is about to crash into. Real life implementation is an attempt to make a robust system capable
of detecting lanes and warn the users on Indian roads which focuses on analysis through the video captured by the
camera HPW100. Also the collision warning is to be issued through early detection of the obstacles, diversions,
vehicles, trucks which may reduce the collision rate by some extent.
The main purpose of this thesis is to develop a Lane Departure Warning System (LDWS). As part of Automatic
Driver Assistance System (ADAS), LDWS exists to alert the driver when the car is diverting from its original lane.
The LDWS requires 3 major operations. First, the captured image is divided into two parts as a road part and a non
-road part by using the camera geometry information. Then, the inverse perspective mapping is applied to avoid the
disadvantage of perspective effect. Next, a gradient method is used to filter lane marks and Canny edge detection is
applied. Additionally, Hough transform method is used for lane marks detection. Finally, the driver is warned
according to right or left lane departure by using detected lane marks’ angles.
Raspberry Pi is the primary platform that this system will be implemented on. It has various Input/Output (I/O) ports
that allow the developer to utilize to connect peripheral-device and many modules and component have been
designed for it, such as the Camera Module which will be used for a various purpose such as capturing live images
of our system.
There are several problems which need to be solved by the system. First of all, the road condition such as weather
and low light condition that will cause the system not able to detect the lane should be addressed with several image
processing technique. Other than that, this system should be portable and compact enough to be installed on the rear
of a windshield mirror and implemented on a vehicle.

[Uploading What is ADAS system (3).pdf…]()

# An Effective Query System using LLMs and Langchain
Created a Query PDF Question Answering System application utilizing Apache Cassandra, DataStax's Astra DB, LangChain, Streamlit, Python
Enhanced information retrieval capabilities, providing a robust solution for efficient and effective query processing. Chat with multiple PDFs at once.
[Chat-With-Multiple-PDF-Documents-Using-Langchain-And-Google-Gemini.pptx]
[AI_report (1).docx](https://github.com/DevanshShukla1/projects/files/15104152/AI_report.1.docx)

 # Baby monitoring system
 Developed smart baby monitoring system utilizing Viola-Jones algorithm for live face detection.
Monitored room conditions, cry detection, and facial emotions via IoT sensors.
Transferred data to Blynk server for remote monitoring via mobile app.
Enabled remote swing control for baby cradle and real-time notifications for abnormalities
[Smart Cradle.pdf](https://github.com/DevanshShukla1/projects/files/15104035/Smart.Cradle.pdf)



# Usage
Python version 3
```
> pip install -r requirements.txt
> python main_fast.py
```

# [Docs](./docs)
