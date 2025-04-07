from algorithms import linear_regression, kmeans_clustering, isolation_forest_anomaly_detection, zscore_anomaly_detection
from visualizer import plot_histogram, plot_interactive_scatter, combine_visualizations
import pandas
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from scipy.stats import zscore
import matplotlib.pyplot as plt
import os
import time


def load_data():
    # Set the working directory to the data folder
    os.chdir('../data')

    # Load the data
    df = pandas.read_csv('ocean_data.csv')

    return df

# 6. Main Function to Run Analysis and Visualizations
def main():
    # Load the data
    df = load_data()

    # Apply Linear Regression for trend analysis
    df, lr_model, y_pred, future_years, future_anomalies = linear_regression(df)

    # Apply Isolation Forest for anomaly detection
    df, isolation_forest_model = isolation_forest_anomaly_detection(df)
    
    # Apply K-means clustering
    df, kmeans_model = kmeans_clustering(df, n_clusters=4)
    
    # Apply Z-score anomaly detection
    df = zscore_anomaly_detection(df, threshold=2)
    
    
    # Step 5: Visualize the Results
    plot_histogram(df)  # Histogram of anomalies distribution
    plot_interactive_scatter(df)  # Interactive scatter plot with Plotly
    
    # Combined Visualizations
    combine_visualizations(df, kmeans_model)  # Combined visualizations (Line plot, Box plot, Clustering)

if __name__ == "__main__":
    main()
