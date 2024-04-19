import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

# Step 1: Collect Data
data = [
    ['Milk', 'Bread', 'Butter'],
    ['Bread', 'Eggs', 'Cheese'],
    ['Milk', 'Bread', 'Eggs']
]

# Step 2: Data Preprocessing
df = pd.DataFrame(data, columns=['Item1', 'Item2', 'Item3'])

# Convert data into one-hot encoded format
one_hot_encoded_data = pd.get_dummies(df)

# Step 3: Association Rule Mining
frequent_itemsets = apriori(one_hot_encoded_data, min_support=0.1, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Step 4: Interpretation and Visualization
print(rules)
