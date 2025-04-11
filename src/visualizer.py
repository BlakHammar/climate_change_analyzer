import plotly.express as px

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
    




