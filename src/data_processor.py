import requests
import pandas

# Fetch the data
ocean_api_url = 'https://global-warming.org/api/ocean-warming-api'

df_cache = None

def load_data():
    global df_cache
    if df_cache is not None: #Check if data frame has already been loaded and cached
        return df_cache
    
    try:
        response = requests.get(ocean_api_url)
        ocean_data = response.json()

    #Extract the data from the 'result' key
        ocean_data = ocean_data.get('result', {})

    # Process the data

        data_list = []
        for year, data in ocean_data.items():
            data_list.append({'Year': year, 'Anomaly': data['anomaly']})    #puts the data into a dictionary

    # Create a DataFrame
        df = pandas.DataFrame(data_list) 
        df_cache = df #Cache dataframe so the request only happens once
        return df
    except requests.exceptions.RequestException as e:
        # Handle any exception that occurs during the request
        print(f"Failed to retrieve data: {e}")
        return None

