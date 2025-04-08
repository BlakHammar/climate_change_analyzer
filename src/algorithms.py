import pandas
import os

def load_data():
    # Set the working directory to the data folder
    os.chdir('../data')

    # Load the data
    df = pandas.read_csv('ocean_data.csv')

    return df