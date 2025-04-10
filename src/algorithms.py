import pandas
import requests
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cluster import KMeans

def load_data():

    # Fetch the data
    response = requests.get("https://global-warming.org/api/ocean-warming-api")
    ocean_data = response.json()

    # Extract the data from the 'result' key
    ocean_data = ocean_data.get('result', {})

    # Process the data
    data_list = []
    for Year, data in ocean_data.items():
        data_list.append({'Year': Year, 'Anomaly': data['anomaly']})

    # Create a DataFrame
    df = pandas.DataFrame(data_list)

    return df


def linear_regression(df):
    #plot the data

    X = df[['Year']]
    y = df['Anomaly']

    #Create a linear regression model
    model = LinearRegression()
    model.fit(X, y)

    #make predictions
    y_pred = model.predict(X)

    # Generate future years (let's forecast for the next 100 years)
    df['Year'] = pandas.to_numeric(df['Year'], errors='coerce')  # Convert to numeric, replacing invalid values with NaN
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


    return df

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
    
    return df
