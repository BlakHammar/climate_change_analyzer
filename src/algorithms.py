import pandas
import matplotlib.pyplot  as plt
import os

from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans, DBSCAN
from sklearn.ensemble import IsolationForest
from scipy.stats import zscore


def linear_regression(df):
    #plot the data

    X = df[['Year']]
    y = df['Anomaly']

    #Create a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    #make predictions
    y_pred = model.predict(X)

    # Generate future years (let's forecast for the next 10 years)
    future_years = pandas.DataFrame({'Year': range(df['Year'].max() + 1, df['Year'].max() + 101)})

    # Predict future anomalies
    future_anomalies = model.predict(future_years)



    # Plot the actual data vs the predicted trend line
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['Anomaly'], color='blue', label='Actual Data')
    plt.plot(df['Year'], y_pred, color='red', label='Trend Line')


    # Plot the forecasted data
    plt.plot(future_years['Year'], future_anomalies, color='green', label='Forecasted Data')

    plt.title('Ocean Anomalies Over Time with Trend Line and Forecast')
    plt.xlabel('Year')
    plt.ylabel('Anomaly')
    plt.legend()
    plt.grid(True)
    plt.show()

    #print the slope
    slope = model.coef_[0]
    print(f"The slope of the trend line is: {slope}")

    # Print the forecasted anomalies for the next 100 years
    for year, anomaly in zip(future_years['Year'], future_anomalies):
        print(f"Forecasted anomaly for year {year}: {anomaly.round(4)}")


    return df, model, y_pred, future_years, future_anomalies



def kmeans_clustering(df, n_clusters=4):
    X = df[['Anomaly']]  # Use anomaly data for clustering
    
    # Create and fit the K-means model
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    df['Cluster'] = kmeans.fit_predict(X)

    # Manually adjust the color assignments to match the plot
    # Here we swap clusters manually: swap cluster 1 and cluster 2
    df['Cluster'] = df['Cluster'].map({0: 0, 1: 2, 2: 1, 3: 3}) 
    
    # Plot clustered data
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['Anomaly'], c=df['Cluster'], cmap='viridis_r')
    plt.title('Ocean Anomalies with K-means Clustering')
    plt.xlabel('Year')
    plt.ylabel('Anomaly')
    plt.colorbar(label='Cluster')
    plt.grid(True)
    plt.show()
    
    return df, kmeans

# Function for Anomaly Detection with Isolation Forest
def isolation_forest_anomaly_detection(df):
    X = df[['Anomaly']]
    
    # Create and fit the Isolation Forest model
    model = IsolationForest(contamination=0.1, random_state=42)
    df['Anomaly_Flag'] = model.fit_predict(X)
    
    # Plot anomalies based on Isolation Forest
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['Anomaly'], c=df['Anomaly_Flag'], cmap='coolwarm')
    plt.title('Ocean Anomalies with Isolation Forest Anomaly Detection')
    plt.xlabel('Year')
    plt.ylabel('Anomaly')
    plt.colorbar(label='Anomaly (1=normal, -1=outlier)')
    plt.grid(True)
    plt.show()
    
    # Show detected anomalies (outliers)
    anomalies = df[df['Anomaly_Flag'] == -1]
    print("Detected Anomalies (outliers):")
    print(anomalies)
    
    return df, model

# Function for Anomaly Detection using Z-score
def zscore_anomaly_detection(df, threshold=2):
    df['Z-score'] = zscore(df['Anomaly'])
    df['Anomaly_Flag'] = (df['Z-score'].abs() > threshold).astype(int)
    
    # Plot anomalies based on Z-score
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['Anomaly'], c=df['Anomaly_Flag'], cmap='coolwarm')
    plt.title('Ocean Anomalies with Z-score Anomaly Detection')
    plt.xlabel('Year')
    plt.ylabel('Anomaly')
    plt.colorbar(label='Anomaly (1=outlier, 0=normal)')
    plt.grid(True)
    plt.show()
    
    # Show detected anomalies
    anomalies = df[df['Anomaly_Flag'] == 1]
    print("Detected Anomalies (outliers based on Z-score):")
    print(anomalies)
    
    return df