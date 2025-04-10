import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

from algorithms import Linear_Regression
from sklearn.model_selection import train_test_split


def scatter_plot(df):
    fig = px.scatter(df, x='Year', y='Anomaly', title='Ocean Anomalies Scatter Plot')

    fig.update_traces(marker=dict(size=16,
                                  line=dict(width=2,
                                            color='DarkSlateGray')),
                        selector=dict(mode='markers'))
    
    fig.update_layout(
    font=dict(color='black', size=24),
    title=dict(
        text='Ocean Anomalies',
        x=0.5,
        xanchor='center'))

    fig.show()


def line_graph(df):
    fig = px.line(df, x='Year', y='Anomaly', title='Ocean Anomalies')

    # Customize the layout
    fig.update_layout(
        font=dict(color='white', size=24),
        xaxis=dict(
            title='Year',
            title_font=dict(color='black', size=24)
        ),
        yaxis=dict(
            title='Anomaly',
            title_font=dict(color='black', size=24)
        ),
        title=dict(
            text='Ocean Anomalies',
            x=0.5,
            xanchor='center')
            ),
    

    fig.show()

def bar_graph(df):
    

    fig = px.bar(df, x='Year', y='Anomaly', title='Ocean Anomalies')

    # Customize the layout
    fig.update_layout(
        font=dict(color='black', size=24),  # Set font color and size
        xaxis=dict(
            title='Year',  # Set x-axis title
            title_font=dict(color='black', size=24),
            tickangle=45,  # Rotate the x-axis labels for better readability
            showgrid=True,  # Show grid lines for better visibility
        ),
        yaxis=dict(
            title='Anomaly',  # Set y-axis title
            title_font=dict(color='black', size=24),
            showgrid=True  # Show grid lines for better visibility
        ),
        title=dict(
            text='Ocean Anomalies',  # Title text
            x=0.5,  # Center the title
            xanchor='center',
            yanchor='top',  # Ensure the title is placed at the top
            font=dict(size=28, color='black')  # Customize title font
        ),
        plot_bgcolor='white',  # Set background color to white
    )

    # Show the plot
    fig.show()
    
def linear_regression(df):

    X = df['Year']
    y = df['Anomaly']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    fig = plt.figure(figsize=(10, 6))
    plt.scatter(X, y, color='b', marker='o', s=30)
    plt.show()


    lr = Linear_Regression()
    lr.fit(X, y)


    y_pred = lr.predict(X)
    cmap = plt.get_cmap('viridis')
    fig = plt.figure(figsize=(10, 6))
    m1 =plt.scatter(X_train, y_train, color=cmap(0.9), s=10)
    m2 = plt.scatter(X_test, y_test, color=cmap(0.5), s=10)

    plt.xlabel('Year')
    plt.ylabel('Anomaly')
    plt.title('Ocean Anomalies with Linear Regression')

    plt.plot(X, y_pred, color='black', linewidth=2, label='Predictions')

    plt.show()



