import numpy as np
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions

# Load pre-trained VGG16 model
model = VGG16(weights='imagenet')

# Define a function to classify an image
def classify_image(image_path):
    # Load and preprocess the image
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # Predict the class of the image
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # Print the top 3 predictions
    print("Top predictions:")
    for _, label, score in decoded_predictions:
        print(f"{label}: {score:.2f}")

# Test the function with an example image
image_path = "example_image.jpg"
classify_image(image_path)
