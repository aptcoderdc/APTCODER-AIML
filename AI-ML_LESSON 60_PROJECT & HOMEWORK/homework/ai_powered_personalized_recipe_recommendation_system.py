# Import necessary libraries
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

# Import machine learning libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Dummy recipe database with additional information
recipes = {
    'spaghetti': {'category': 'Italian', 'difficulty': 'Medium', 'ingredients': ['spaghetti', 'tomato sauce', 'ground beef'], 'instructions': 'Boil spaghetti. Brown ground beef. Mix with tomato sauce.'},
    'chicken_curry': {'category': 'Indian', 'difficulty': 'Medium', 'ingredients': ['chicken', 'curry powder', 'coconut milk'], 'instructions': 'Cook chicken with curry powder. Add coconut milk and simmer.'},
    'caesar_salad': {'category': 'Salad', 'difficulty': 'Easy', 'ingredients': ['lettuce', 'croutons', 'parmesan cheese'], 'instructions': 'Mix lettuce with croutons and parmesan cheese. Add caesar dressing.'},
    'stir_fry': {'category': 'Asian', 'difficulty': 'Medium', 'ingredients': ['vegetables', 'soy sauce', 'chicken'], 'instructions': 'Stir-fry vegetables and chicken in soy sauce.'},
    'pizza': {'category': 'Italian', 'difficulty': 'Easy', 'ingredients': ['dough', 'tomato sauce', 'cheese'], 'instructions': 'Spread tomato sauce on dough. Add cheese and bake.'}
}

# Function to process user query using NLP
def process_query(query):
    tokens = word_tokenize(query.lower())
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens

# Function to recommend recipes based on user preferences
def recommend_recipe(user_preferences):
    # Dummy code for recipe recommendation
    # Placeholder for machine learning model prediction
    # Generate dummy data
    X = np.random.rand(100, 10)  # 100 samples, 10 features
    y = np.random.choice(list(recipes.keys()), size=100)  # Recipe labels
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Initialize and train the classifier
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    # Evaluate the classifier
    accuracy = clf.score(X_test, y_test)
    # Get recommended recipe based on user preferences
    recommended_recipe = clf.predict(user_preferences.reshape(1, -1))[0]
    return recommended_recipe, accuracy

# Function to provide detailed information about the recommended recipe
def get_recipe_details(recipe_name):
    return recipes.get(recipe_name, "Recipe details not found")

# Function to display image of the recommended recipe
def display_recipe_image(recipe_name):
    # Dummy code to display image
    # Placeholder for loading and displaying recipe image
    pass

# Function to visualize recipe categories distribution
def visualize_recipe_categories():
    categories = [recipe['category'] for recipe in recipes.values()]
    category_counts = {category: categories.count(category) for category in set(categories)}
    plt.figure(figsize=(8, 6))
    plt.bar(category_counts.keys(), category_counts.values())
    plt.title('Recipe Categories Distribution')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Function to visualize recipe difficulties distribution
def visualize_recipe_difficulties():
    difficulties = [recipe['difficulty'] for recipe in recipes.values()]
    difficulty_counts = {difficulty: difficulties.count(difficulty) for difficulty in set(difficulties)}
    plt.figure(figsize=(8, 6))
    plt.pie(difficulty_counts.values(), labels=difficulty_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Recipe Difficulties Distribution')
    plt.show()

# Example usage
visualize_recipe_categories()
visualize_recipe_difficulties()

# Example usage
user_query = "I want an easy Italian recipe with spaghetti"
processed_query = process_query(user_query)
print("Processed Query:", processed_query)

user_preferences = np.random.rand(10)  # User preferences vector
recommended_recipe, accuracy = recommend_recipe(user_preferences)
print("Recommended Recipe:", recommended_recipe)

recipe_details = get_recipe_details(recommended_recipe)
print("Recipe Details:", recipe_details)

display_recipe_image(recommended_recipe)

