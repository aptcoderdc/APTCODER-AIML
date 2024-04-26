import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Sample data for sentiment analysis
texts = ["I love this movie!", "This movie is terrible.", "The acting was superb.", "I didn't like the plot."]
labels = [1, 0, 1, 0]  # 1 for positive, 0 for negative sentiment

# Initialize tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)  # 2 classes: positive, negative

# Tokenize inputs
inputs = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')

# Train the model
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
model.train()
optimizer.zero_grad()
outputs = model(**inputs, labels=torch.tensor(labels).unsqueeze(0))
loss = outputs.loss
loss.backward()
optimizer.step()

# Evaluate the model
model.eval()
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predictions = torch.argmax(logits, dim=1).tolist()

print("Predictions:", predictions)
