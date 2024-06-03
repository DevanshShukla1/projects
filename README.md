# LDWS

The Lane Departure Warning System (LDWS) and Collision Warning System are critical components of Advanced Driver Assistance Systems (ADAS), enhancing safety and preventing accidents on roads. This thesis focuses on the development and implementation of these systems, both in prototype and real-life scenarios, with a particular emphasis on their application in Indian road conditions.

# Prototype Implementation:
The prototype car is equipped with various sensors and cameras to detect lane markings and obstacles. The lane departure warning system utilizes OpenCV and deep learning techniques for lane detection. When the prototype crosses a lane without signaling, it issues a departure warning to alert the driver. Similarly, the collision warning system employs ultrasonic and IR sensors to detect obstacles in the vehicle's path. This early warning system alerts the driver of potential collisions, helping to prevent accidents.

The Raspberry Pi 4 B board serves as the primary platform for processing camera video and implementing these systems. Its versatile I/O ports facilitate the connection of peripheral devices, such as the Camera Module, which captures live images for analysis. By combining computer vision algorithms and sensor data, the prototype demonstrates the feasibility of LDWS and collision warning systems in a controlled environment.

# Real-Life Implementation:
The real-life implementation aims to create a robust system capable of detecting lanes and issuing warnings in the challenging conditions of Indian roads. The HPW100 camera captures video footage, which undergoes extensive analysis to detect lane markings and potential obstacles.

The LDWS operates through several key steps:

Image Processing: The captured image is divided into road and non-road parts using camera geometry information. This separation helps focus the analysis on relevant lane markings.
Perspective Correction: Inverse perspective mapping corrects for the distortion caused by the camera angle, ensuring accurate lane detection.
Lane Detection: A gradient method filters lane markings, and Canny edge detection further refines the detection process. The Hough transform method identifies lane markings accurately.
Warning Generation: Based on the detected lane marks' angles, the system determines whether the vehicle is drifting left or right and issues appropriate warnings to the driver.
In addition to the LDWS, the collision warning system utilizes sensor data to detect potential hazards, including obstacles, diversions, vehicles, and trucks. Early detection of these hazards allows the system to warn the driver promptly, reducing the likelihood of collisions.

# Conclusion:
The development and implementation of LDWS and collision warning systems represent significant strides in enhancing road safety through ADAS technology. While the prototype demonstrates the feasibility of these systems, the real-life implementation addresses the challenges of operating in diverse and dynamic road environments, such as those found in India. By combining advanced algorithms with sensor data, these systems provide drivers with timely warnings, mitigating the risk of accidents and improving overall road safety. As technology continues to evolve, further advancements in ADAS systems hold the promise of even greater safety benefits for drivers and pedestrians alike.

[What is ADAS system (3).pdf](https://github.com/DevanshShukla1/projects/files/15137832/What.is.ADAS.system.3.pdf)


# An Effective Query System using LLMs and Langchain
Created a Query PDF Question Answering System application utilizing Apache Cassandra, DataStax's Astra DB, LangChain, Streamlit, Python
Enhanced information retrieval capabilities, providing a robust solution for efficient and effective query processing. Chat with multiple PDFs at once.
[Chat-With-Multiple-PDF-Documents-Using-Langchain-And-Google-Gemini.pptx]



 # Smart Infant Cradle 
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
