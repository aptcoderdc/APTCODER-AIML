# AI-powered Personalized Recipe Recommendation System

## Overview
This project is an AI-powered personalized recipe recommendation system that recommends recipes based on user preferences. It leverages machine learning algorithms for predictive analysis and provides visualizations for better insights into recipe categories and difficulties.

## Concepts Covered
- Natural Language Processing (NLP) for user query processing
- Machine learning algorithms for recipe recommendation
- Data visualization for recipe categories distribution and difficulties

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

python recipe_recommendation_system.py

## Example Usage

# Example usage of the recipe recommendation system functions
user_query = "I want an easy Italian recipe with spaghetti"
processed_query = process_query(user_query)
print("Processed Query:", processed_query)

user_preferences = np.random.rand(10)  # User preferences vector
recommended_recipe, accuracy = recommend_recipe(user_preferences)
print("Recommended Recipe:", recommended_recipe)

recipe_details = get_recipe_details(recommended_recipe)
print("Recipe Details:", recipe_details)

display_recipe_image(recommended_recipe)