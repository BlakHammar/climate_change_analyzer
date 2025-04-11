import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from src.algorithms import linear_regression, kmeans_clustering, detect_anomalies

class test_algorithms(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({ #sample data for data frame
            'Year': list(range(2000,2010)),
            'Anomaly': [0.1, 0.15, 0.2, 0.3, 0.35, 0.4, 0.38, 0.45, 0.5, 0.55]
        })

    @patch("matplotlib.pyplot.show") #hide graph from appearing
    @patch("builtins.print") #hide print statements (slope is printed)
    def test_linregress(self, mock_print , mock_show):
        updated_df = linear_regression(self.df.copy())

        self.assertTrue(pd.api.types.is_numeric_dtype(updated_df['Year'])) #Check for year column and ensure its numeric
        self.assertTrue(any("slope of the trend line" in str(call) for call in mock_print.call_args_list)) #Check if slope was printed (means regression line was calculated and created)
        self.assertEqual(len(updated_df), len(self.df)) #check # of rows is consistent

    @patch("matplotlib.pyplot.show")
    def test_kmeans_clustering_output(self, mock_show):
        clustered_df = kmeans_clustering(self.df.copy(), n_clusters=4)

        self.assertIn('Cluster', clustered_df.columns) #Check for cluster column
        self.assertLessEqual(clustered_df['Cluster'].nunique(), 4) #Check number of clusters
        self.assertTrue(pd.api.types.is_integer_dtype(clustered_df['Cluster'])) #Check if all clusters are ints

    @patch("matplotlib.pyplot.show") 
    def test_anomaly_detection(self, mock_show):
        years = np.arange(1850, 2025) #Create years
        anomaly = [0.0] * len(years) #Create baseline annual anomaly values
        anomaly[30] = 1.0   # create outlier anomaly in 1880
        anomaly[50] = -1.0  # create outlier anomaly in 1990

        df = pd.DataFrame({'Year': years, 'Anomaly': anomaly}) #create data frame

        anomalies = detect_anomalies(df, windowSize=15, threshold=2.0) #run anomaly detection

        expected_anomalies = [(1880, 1.0), (1900, -1.0)] #
        self.assertEqual(len(anomalies), 2) #check only 2 anomalies were found (created above)
        self.assertTrue(all(anomaly in anomalies for anomaly in expected_anomalies)) #check the expected anomalies with detected anomalies
        
        mock_show.assert_called_once() #ensure graph was displayed

if __name__ == '__main__':
    unittest.main()