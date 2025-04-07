import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px
from sklearn.cluster import KMeans


# Histogram of Ocean Anomalies
def plot_histogram(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df['Anomaly'], bins=30, color='skyblue', edgecolor='black')
    plt.title('Distribution of Ocean Anomalies')
    plt.xlabel('Anomaly')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()



# Interactive Scatter Plot using Plotly
def plot_interactive_scatter(df):
    fig = px.scatter(df, x='Year', y='Anomaly', color='Cluster', 
                     title='Interactive Ocean Anomalies with Clustering',
                     labels={'Year': 'Year', 'Anomaly': 'Anomaly'})
    fig.show()


# Combine Multiple Visualizations (Line Plot, Box Plot, and Clusters)
def combine_visualizations(df, kmeans):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Line plot
    axes[0].plot(df['Year'], df['Anomaly'], color='blue')
    axes[0].set_title('Ocean Anomalies Over Time')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Anomaly')

    # Box plot
    axes[1].boxplot(df['Anomaly'], vert=False, patch_artist=True)
    axes[1].set_title('Box Plot of Anomalies')

    # Clustering with centroids (1D centroids)
    axes[2].scatter(df['Year'], df['Anomaly'], c=df['Cluster'], cmap='viridis')
    
    # Plot centroids (1D)
    centroids = kmeans.cluster_centers_

    # Plot each centroid on the plot at the first Year of each cluster's Anomaly
    for i, centroid in enumerate(centroids):
        # Find the Year closest to the centroid's value
        closest_year_idx = (df['Anomaly'] - centroid).abs().argmin()
        closest_year = df['Year'].iloc[closest_year_idx]
        
        # Plot the centroid at the closest Year and its Anomaly value
        axes[2].scatter(closest_year, centroid, c='red', s=100, marker='X', label=f'Centroid {i+1}' if i == 0 else "")

    axes[2].set_title('Clustering with Centroids')
    axes[2].legend()

    plt.tight_layout()
    plt.show()


