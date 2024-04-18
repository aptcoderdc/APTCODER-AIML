from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# Sample data
weather = ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny', 'sunny', 'rainy']
temperature = ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool', 'mild', 'cool', 'mild']
ice_creams_sold = [20, 25, 30, 10, 15, 12, 28, 22, 18, 10]

# Convert categorical variables to numerical
weather_encoder = LabelEncoder()
temperature_encoder = LabelEncoder()

weather_encoded = weather_encoder.fit_transform(weather)
temperature_encoded = temperature_encoder.fit_transform(temperature)

# Combine features into a single array
features = list(zip(weather_encoded, temperature_encoded))

# Decision Tree
tree_model = DecisionTreeRegressor()
tree_model.fit(features, ice_creams_sold)

# Random Forest
forest_model = RandomForestRegressor(n_estimators=100)
forest_model.fit(features, ice_creams_sold)

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
