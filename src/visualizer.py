import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import pandas


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
    plt = px.scatter(df, x='Year', y='Anomaly', color='Cluster', 
                     title='Interactive Ocean Anomalies with Clustering',
                     labels={'Year': 'Year', 'Anomaly': 'Anomaly'})
    plt.show()


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



