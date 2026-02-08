# Driver Drowsiness Detection using Computer Vision

A real-time computer vision system that detects driver drowsiness by monitoring eye closure through a webcam and provides both visual and audio alerts when prolonged eye closure is detected.

## Project Overview
Driver fatigue is a major cause of road accidents. This project aims to improve road safety by identifying early signs of drowsiness using computer vision techniques. The system continuously monitors the driver’s eyes and triggers an alert if the eyes remain closed for a specified duration.

The application runs in real time and is designed as a lightweight, practical safety system.

## Approach
1. Capture live video feed from a webcam
2. Convert video frames to grayscale
3. Detect face regions using Haar cascade classifiers
4. Detect eyes within the face region
5. Monitor eye visibility over consecutive frames
6. Identify drowsiness based on prolonged eye closure
7. Trigger visual and audio alerts when drowsiness is detected

## Technologies Used
- Python
- OpenCV
- Haar Cascade Classifiers
- NumPy
- Windows `winsound` module for audio alerts

## How to Run

### Install dependencies
```bash
pip install -r requirements.txt
