# Text Classification with Naive Bayes

## Overview
This project demonstrates text classification using a Naive Bayes classifier implemented with scikit-learn in Python. We'll classify text samples into two categories: positive and negative sentiment.

## Dependencies
- Python (>= 3.6)
- scikit-learn (>= 0.24.0)

You can install the required dependencies using pip:
```bash
pip install scikit-learn
Dataset
For simplicity, we use a small sample dataset containing text samples with corresponding sentiment labels (0 for negative, 1 for positive). You can replace this dataset with your own data for more comprehensive analysis.

Usage
Clone this repository:

git clone https://github.com/your_username/text-classification-naive-bayes.git
cd text-classification-naive-bayes
Install dependencies:

pip install -r requirements.txt
Run the text classification script:

python text_classification.py

Configuration
You can modify the following parameters in the text_classification.py script to customize the behavior:

texts: Input text samples for classification.
labels: Corresponding sentiment labels (0 for negative, 1 for positive).
test_size: Size of the test set during data splitting.
random_state: Seed for the random number generator.