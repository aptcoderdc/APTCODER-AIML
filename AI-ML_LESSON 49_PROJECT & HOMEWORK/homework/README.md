# Object Detection Homework with YOLO

## Overview
This homework assignment involves implementing object detection using YOLO (You Only Look Once) algorithm. The task is to detect objects in an image and provide confidence scores for each detection.

## Concepts Covered
- Object Detection
- YOLO (You Only Look Once)
- Bounding Box Detection
- Confidence Scores
- Dummy Data Generation

## Required Libraries
- NumPy

## Setup
1. Ensure you have Python installed.
2. Install the required libraries:

   pip install numpy

## How to Run
Clone the repository or create a new Python script.
Copy and paste the provided code into your Python script.
Run the Python script:

python object_detection_homework.py

## Homework Structure
object_detection_homework.py: Python script containing the implementation of object detection homework with YOLO.
README.md: Overview, concepts covered, required libraries, setup, and how to run instructions for the homework.

## Usage
The detect_objects_homework(image) function takes an image array as input and returns a list of detected objects along with their labels, bounding box coordinates, and confidence scores. The dummy implementation randomly generates bounding box coordinates and confidence scores for the predefined set of objects.

## Example Output

Detected Objects (Homework):
Label: person, Bounding Box: (265, 89, 298, 122), Confidence: 0.82
Label: car, Bounding Box: (368, 323, 409, 356), Confidence: 0.65
Label: dog, Bounding Box: (17, 243, 49, 275), Confidence: 0.77
Label: cat, Bounding Box: (396, 48, 432, 77), Confidence: 0.68