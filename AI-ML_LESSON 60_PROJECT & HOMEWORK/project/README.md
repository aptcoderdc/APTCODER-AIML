# AI-powered Smart Garden Assistant

## Overview
This project is an AI-powered smart garden assistant that helps users with plant identification, health monitoring, pest detection, and companion plant recommendations. It leverages machine learning algorithms for predictive analysis and provides visualizations for better insights into plant categories and health statuses.

## Concepts Covered
- Natural Language Processing (NLP) for user query processing
- Computer vision for plant identification
- Machine learning algorithms for plant health monitoring and pest detection
- Data visualization for plant categories distribution and health statuses

## Required Libraries
- nltk
- numpy
- opencv-python
- scikit-learn
- matplotlib

## Setup
1. Clone the repository to your local machine.
2. Install the required libraries using pip:

pip install -r requirements.txt

3. Download NLTK data by running the following commands in Python:

import nltk
nltk.download('punkt')
nltk.download('stopwords')

## How to Run
Ensure that you have Python installed on your system.
Open a terminal or command prompt.
Navigate to the project directory.
Run the main script:

python smart_garden_assistant.py

## Example Usage

# Example usage of the smart garden assistant functions
user_query = "What's wrong with my tomato plant?"
processed_query = process_query(user_query)
print("Processed Query:", processed_query)

image_path = "plant_image.jpg"  # Path to the uploaded image
identified_plant = identify_plant(image_path)
print("Identified Plant:", identified_plant)

health_status = monitor_plant_health(image_path)
print("Plant Health Status:", health_status)

pests_detected = detect_pests(image_path)
print("Pests Detected:", pests_detected)

plant_details = get_plant_details(identified_plant)
print("Plant Details:", plant_details)

companion_plants = recommend_companion_plants(identified_plant)
print("Companion Plants:", companion_plants)

# Visualize plant categories distribution
visualize_plant_categories()

# Visualize plant health statuses distribution
visualize_plant_health_statuses()