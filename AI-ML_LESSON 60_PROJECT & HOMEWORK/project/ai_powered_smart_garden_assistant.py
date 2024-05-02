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

# Dummy plant database with additional information
plants = {
    'tomato': {'category': 'vegetable', 'price': 2.99, 'description': 'Red, juicy tomatoes'},
    'basil': {'category': 'herb', 'price': 1.99, 'description': 'Aromatic basil leaves'},
    'rosemary': {'category': 'herb', 'price': 1.49, 'description': 'Fragrant rosemary sprigs'},
    'sunflower': {'category': 'flower', 'price': 0.99, 'description': 'Bright, yellow sunflowers'},
    'mint': {'category': 'herb', 'price': 1.29, 'description': 'Refreshing mint leaves'}
}

# Function to process user query using NLP
def process_query(query):
    tokens = word_tokenize(query.lower())
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens

# Function to identify plants from images using computer vision
def identify_plant(image_path):
    # Dummy code for plant identification from image
    image = cv2.imread(image_path)
    # Placeholder for computer vision processing
    # Here, we'll just return a random plant for demonstration purposes
    return random.choice(list(plants.keys()))

# Function for plant health monitoring using machine learning
def monitor_plant_health(plant_image):
    # Dummy code for plant health monitoring
    # Placeholder for machine learning model prediction
    # Generate dummy data
    X = np.random.rand(100, 10)  # 100 samples, 10 features
    y = np.random.randint(2, size=100)  # Binary labels
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Initialize and train the classifier
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    # Evaluate the classifier
    accuracy = clf.score(X_test, y_test)
    return accuracy

# Function for pest detection using machine learning
def detect_pests(plant_image):
    # Dummy code for pest detection
    # Placeholder for machine learning model prediction
    # Generate dummy data
    X = np.random.rand(100, 10)  # 100 samples, 10 features
    y = np.random.randint(2, size=100)  # Binary labels
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Initialize and train the classifier
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    clf = SVC()
    clf.fit(X_train_scaled, y_train)
    # Evaluate the classifier
    accuracy = clf.score(X_test_scaled, y_test)
    return accuracy

# Function to provide detailed information about the identified plant
def get_plant_details(plant_name):
    return plants.get(plant_name, "Plant details not found")

# Function to recommend companion plants based on the identified plant
def recommend_companion_plants(plant_name):
    # Dummy code for companion planting recommendations
    # Placeholder for recommending plants that grow well together
    return "Consider planting these companions with your " + plant_name + ": basil, marigold"

# Function to visualize plant categories distribution
def visualize_plant_categories():
    categories = [plant['category'] for plant in plants.values()]
    category_counts = {category: categories.count(category) for category in set(categories)}
    plt.figure(figsize=(8, 6))
    plt.bar(category_counts.keys(), category_counts.values())
    plt.title('Plant Categories Distribution')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.show()

# Function to visualize plant health statuses distribution
def visualize_plant_health_statuses():
    health_statuses = ['Healthy', 'Unhealthy']
    health_status_counts = {'Healthy': 75, 'Unhealthy': 25}  # Dummy counts
    plt.figure(figsize=(8, 6))
    plt.pie(health_status_counts.values(), labels=health_status_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Plant Health Statuses Distribution')
    plt.show()

# Example usage
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

# Example usage
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
