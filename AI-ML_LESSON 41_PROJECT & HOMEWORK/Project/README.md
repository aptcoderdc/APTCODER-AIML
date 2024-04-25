


Neural Network Model for Iris Dataset:-


This project demonstrates building a simple neural network model for the Iris dataset using Scikit-learn. The Iris dataset is a well-known dataset in the machine learning community and consists of samples of iris flowers with four features each: sepal length, sepal width, petal length, and petal width.

Project Overview
1. Dataset Preparation:
The Iris dataset is loaded using Scikit-learn's load_iris function.
The dataset is split into training and testing sets using the train_test_split function.

2. Model Development:
A simple neural network model is built using Scikit-learn's MLPClassifier.
The model consists of a single hidden layer with 10 neurons, ReLU activation function, Adam optimizer, and a maximum of 1000 iterations.
The model is trained on the training data.

3. Model Evaluation:
The trained model is evaluated on the testing data using the score method.
The accuracy of the model on the testing data is printed to the console.

4. Conclusion:
The project concludes with a summary of the model's performance and its completion.

Usage
Clone the repository:

git clone <repository_url>
cd <repository_name>
Install the required dependencies:

pip install scikit-learn

Run the Python script to execute the project:

python neural_network_iris.py


Requirements
Python 3.x
Scikit-learn