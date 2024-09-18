Sign Language Detection Project

Introduction
The Sign Language Detection project aims to bridge communication gaps for individuals with hearing impairments by developing an automated system that detects and interprets sign language gestures in real-time. This Python-based project leverages Scikit Learn, OpenCV, and MediaPipe to create a robust machine learning system capable of recognizing hand gestures and translating them into text.


Key Features:
Image Saving: Uses a webcam to capture sign language gestures and store them in a dataset for model training.
Dataset Preparation: Extracts hand landmarks from images using MediaPipe and prepares the dataset for training.
Model Training: Trains a Random Forest classifier using the extracted features.
Real-time Testing: Implements the trained model to perform real-time gesture recognition using live video feed.


Methodology:
Data Collection: Capture sign language images using a webcam and store them in a directory.
Dataset Preparation: Extract hand landmarks and generate feature vectors.
Model Training: Train a Random Forest classifier and evaluate model performance.
Real-time Detection: Use the trained model to predict sign language gestures from live video input.


Aim:
To develop a reliable and efficient sign language detection system that enhances accessibility and inclusivity for individuals with hearing impairments.
