# OpenCV Project - Finger Counter
---
### This is a simple Python program that uses the MediaPipe library along with OpenCV to count the number of fingers displayed in front of a webcam. It detects hand landmarks and estimates the finger count based on the position of the thumb and fingers.
---

# How it Works
---
### 1. The program uses the MediaPipe library to detect hand landmarks (21 points) in each frame captured from the webcam.
### 2. It then calculates the distance between the thumb and the tip of the index finger.
### 3. If this distance is larger than a threshold value, it considers the thumb as extended (finger = 1), otherwise not (finger = 0).
### 4. Similarly, it checks the position of the tips of the other four fingers with respect to lower-hand landmarks to determine if they are extended or not.
### 5. Based on the number of extended fingers, the program displays the finger count on the video feed.
