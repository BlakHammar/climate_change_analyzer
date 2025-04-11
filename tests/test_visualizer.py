import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import plotly.graph_objects as go
from src.visualizer import scatter_plot, line_graph, bar_graph

class visua_test(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.DataFrame({ #setUp data used for testing graph creation
            'Year': [2000, 2001, 20002],
            'Anomaly': [0.1, 0.2, 0.15]
        })
    
    @patch('src.visualizer.px.scatter') #Test to see if scatter plot is properly being created
    def test_scatter(self, mock_show):
        mock_fig = MagicMock() #Mock graph so real one doesn't appear
        mock_show.return_value = mock_fig
        scatter_plot(self.df)
        mock_show.assert_called_once_with(self.df, x='Year', y='Anomaly', title='Ocean Anomalies Scatter Plot') #Ensure the mock graph has these features

    @patch('src.visualizer.px.line') #Test to see if line graph is properly being created
    def test_line(self, mock_show):
        mock_fig = MagicMock() #Mock graph so real one doesn't appear
        mock_show.return_value = mock_fig
        line_graph(self.df)
        mock_show.assert_called_once_with(self.df, x='Year', y='Anomaly', title='Ocean Anomalies') #Ensure the mock graph has these features

    @patch('src.visualizer.px.bar') #Test to see if bar graph is properly being created
    def test_bar(self, mock_show):
        mock_fig = MagicMock() #Mock graph so real one doesn't appear
        mock_show.return_value = mock_fig
        bar_graph(self.df)
        mock_show.assert_called_once_with(self.df, x='Year', y='Anomaly', title='Ocean Anomalies') #Ensure the mock graph has these features

if __name__ == "__main__":
    unittest.main()