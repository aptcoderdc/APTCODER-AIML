import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import cv2
import numpy as np
import random  # Add import for random module

# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Dummy product database
products = {
    'iphone': {'category': 'electronics', 'price': 999, 'description': 'Smartphone from Apple'},
    'book': {'category': 'books', 'price': 20, 'description': 'Bestselling novel'},
    'shoes': {'category': 'fashion', 'price': 50, 'description': 'Sports shoes for men'},
    # Add more products as needed
}

# Function to process user query using NLP
def process_query(query):
    tokens = word_tokenize(query.lower())
    tokens = [word for word in tokens if word.isalnum()]
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return tokens

# Function to identify products from images using computer vision
def identify_product(image_path):
    # Dummy code for product identification from image
    image = cv2.imread(image_path)
    # Placeholder for computer vision processing
    # Here, we'll just return a random product for demonstration purposes
    return random.choice(list(products.keys()))

# Example usage
user_query = "I need a smartphone"
processed_query = process_query(user_query)
print("Processed Query:", processed_query)

image_path = "product_image.jpg"  # Path to the uploaded image
identified_product = identify_product(image_path)
print("Identified Product:", identified_product)
print("Product Details:", products[identified_product])
