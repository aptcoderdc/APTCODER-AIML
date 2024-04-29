# Import necessary libraries
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix

# Function to generate synthetic tweet data
def generate_tweets(num_tweets=1000):
    tweets = []
    sentiments = []
    for _ in range(num_tweets):
        tweet = generate_tweet()
        tweets.append(tweet)
        sentiment = generate_sentiment(tweet)
        sentiments.append(sentiment)
    return tweets, sentiments

# Function to generate a synthetic tweet
def generate_tweet():
    positive_words = ['great', 'awesome', 'love', 'happy', 'amazing']
    negative_words = ['hate', 'dislike', 'awful', 'terrible', 'horrible']
    neutral_words = ['okay', 'fine', 'average', 'normal', 'neutral']
    
    sentiment = random.choice(['positive', 'negative', 'neutral'])
    
    if sentiment == 'positive':
        return ' '.join(random.choices(positive_words, k=random.randint(5, 15)))
    elif sentiment == 'negative':
        return ' '.join(random.choices(negative_words, k=random.randint(5, 15)))
    else:
        return ' '.join(random.choices(neutral_words, k=random.randint(5, 15)))

# Function to generate sentiment label based on the tweet
def generate_sentiment(tweet):
    if 'great' in tweet or 'awesome' in tweet or 'love' in tweet or 'happy' in tweet or 'amazing' in tweet:
        return 'positive'
    elif 'hate' in tweet or 'dislike' in tweet or 'awful' in tweet or 'terrible' in tweet or 'horrible' in tweet:
        return 'negative'
    else:
        return 'neutral'

# Generate synthetic tweet data
tweets, sentiments = generate_tweets(num_tweets=1000)

# Feature Engineering
vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(tweets)

# Model training
X_train, X_test, y_train, y_test = train_test_split(X, sentiments, test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluation
predictions = model.predict(X_test)
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))
