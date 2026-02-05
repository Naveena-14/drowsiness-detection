# Driver Drowsiness Detection 🚗💤

A real-time computer vision system that monitors eye closure to detect driver drowsiness using OpenCV and Haar cascade classifiers.

## 📌 Problem Statement
Driver fatigue is a major cause of road accidents. This project detects early signs of drowsiness by continuously monitoring eye activity through a webcam and alerting the user when prolonged eye closure is detected.

## 🧠 Approach
1. Capture real-time video using a webcam
2. Detect face regions using Haar cascades
3. Detect eyes within the face region
4. Monitor eye visibility over consecutive frames
5. Trigger a visual alert if eyes remain closed for a defined duration

## 🛠️ Technologies Used
- Python
- OpenCV
- Haar Cascade Classifiers
- NumPy

## ⚙️ How to Run
```bash
pip install -r requirements.txt
python drowsiness.py
