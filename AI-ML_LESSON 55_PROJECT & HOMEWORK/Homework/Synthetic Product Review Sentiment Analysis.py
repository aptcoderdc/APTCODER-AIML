import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

# Function to generate synthetic product reviews
def generate_reviews(num_reviews=1000):
    reviews = []
    sentiments = []
    for _ in range(num_reviews):
        review = generate_review()
        reviews.append(review)
        sentiment = generate_sentiment(review)
        sentiments.append(sentiment)
    return reviews, sentiments

# Function to generate a synthetic product review
def generate_review():
    review_templates = [
        "This product is {}.", 
        "I {} this product.", 
        "{} product ever!", 
        "I would not recommend this product because it is {}."
    ]
    adjectives = ['great', 'good', 'bad', 'terrible', 'awesome', 'excellent', 'poor', 'amazing']
    
    template = random.choice(review_templates)
    adjective = random.choice(adjectives)
    
    return template.format(adjective)

# Function to generate sentiment label based on the review
def generate_sentiment(review):
    if 'great' in review or 'good' in review or 'excellent' in review or 'awesome' in review or 'amazing' in review:
        return 'positive'
    elif 'bad' in review or 'terrible' in review or 'poor' in review:
        return 'negative'
    else:
        return 'neutral'

# Generate synthetic product review data
reviews, sentiments = generate_reviews(num_reviews=1000)

# Feature Engineering
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(reviews)

# Model training
X_train, X_test, y_train, y_test = train_test_split(X, sentiments, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluation
predictions = model.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
