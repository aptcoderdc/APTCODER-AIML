Step 1: Setup

First, make sure you have Python installed on your computer. You'll also need to install the scikit-learn library if you haven't already. You can install it using pip:
pip install scikit-learn

Step 2: Data Collection

We'll create some sample data representing the weather conditions and the number of ice creams sold. You can create a CSV file with this data or directly define it in your Python code.

# Sample data
weather = ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy']
temperature = ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild']
ice_creams_sold = [20, 25, 30, 10, 15, 12, 28, 22, 18, 10]

Step 3: Data Preprocessing

We need to convert our categorical data (weather and temperature) into numerical format because scikit-learn's decision tree and random forest implementations require numerical input.
from sklearn.preprocessing import LabelEncoder

# Convert categorical variables to numerical
weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()

weather_encoded = weather_encoder.fit_transform(weather)
temperature_encoded = temperature_encoder.fit_transform(temperature)

# Combine features into a single array
features = list(zip(weather_encoded, temperature_encoded))

Step 4: Building Models

Now, let's build decision tree and random forest models using scikit-learn.
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Decision Tree
tree_model = DecisionTreeRegressor()
tree_model.fit(features, ice_creams_sold)

# Random Forest
forest_model = RandomForestRegressor(n_estimators=100)
forest_model.fit(features, ice_creams_sold)

Step 5: Making Predictions

Now that we have trained models, let's make some predictions.

# Make predictions
new_weather = 'sunny'
new_temperature = 'hot'

# Encode new data
encoded_weather = weather_encoder.transform([new_weather])
encoded_temperature = temperature_encoder.transform([new_temperature])

# Combine features
new_features = [[encoded_weather[0], encoded_temperature[0]]]

# Predictions
tree_prediction = tree_model.predict(new_features)
forest_prediction = forest_model.predict(new_features)

print("Predicted Ice Creams Sold (Decision Tree):", tree_prediction[0])
print("Predicted Ice Creams Sold (Random Forest):", forest_prediction[0])

Step 6: Interpretation

You can now interpret the predictions. These models are based on the input weather condition and temperature, and they predict the number of ice creams sold based on patterns learned from the training data.
This project introduces the basics of decision trees and random forests in a simple and fun way for kids! They can experiment with different weather conditions and temperatures to see how it affects the predicted ice cream sales.
