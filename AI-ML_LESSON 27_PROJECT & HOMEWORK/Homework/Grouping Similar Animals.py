import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


# Sample data
data = {
    'Animal': ['Dog', 'Cat', 'Dolphin', 'Elephant', 'Tiger', 'Whale'],
    'Size': ['Medium', 'Small', 'Medium', 'Large', 'Large', 'Extra Large'],
    'Weight': [20, 5, 150, 5000, 250, 20000],
    'Habitat': ['Land', 'Land', 'Water', 'Land', 'Land', 'Water'],
    'Diet': ['Omnivore', 'Carnivore', 'Carnivore', 'Herbivore', 'Carnivore', 'Carnivore']
}


# Create DataFrame
df = pd.DataFrame(data)


# Encode categorical variables
df_encoded = pd.get_dummies(df.drop(columns=['Animal']))


# Perform K-means clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(df_encoded)
labels = kmeans.labels_


# Add cluster labels to DataFrame
df['Cluster'] = labels


# Visualize clusters
plt.scatter(df['Size'], df['Weight'], c=df['Cluster'], cmap='viridis')
plt.xlabel('Size')
plt.ylabel('Weight')
plt.title('Animal Clustering')
plt.show()


# Print clustered animals
print("Clustered Animals:")
for cluster_num in range(kmeans.n_clusters):
    cluster_animals = df[df['Cluster'] == cluster_num]['Animal'].values
    print(f"Cluster {cluster_num + 1}: {', '.join(cluster_animals)}")
