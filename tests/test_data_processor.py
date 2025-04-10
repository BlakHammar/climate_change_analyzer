import unittest
from unittest.mock import patch
import pandas as pd
import numpy as np
import requests
from src.data_processor import load_data
#from src.data_processor import load_data

class testDataProcess(unittest.TestCase):
    def test_data_load(self): #Test data loading ensuring its a panda data frame and has rows
       with patch("requests.get") as mocked_get:
           mocked_get.return_value.status_code = 200
           mocked_get.return_value.json = lambda: {
                'result': {
                    '2020': {'anomaly': 1.23},
                    '2021': {'anomaly': 4.56},
                }
            }
           result_df = load_data()
           self.assertIsInstance(result_df, pd.DataFrame) #check if the result is a data frame
           self.assertEqual(len(result_df), 2) #should have 2 rows 

    def test_data_fail(self): #Test what happens if fetching data through http request fails
        with patch("requests.get") as mocked_get:
            mocked_get.side_effect = requests.exceptions.RequestException("Network Error")
            result_df = load_data()
            self.assertIsNone(result_df)


if __name__ == '__main__':
    unittest.main()