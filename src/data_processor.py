import requests
import pandas

# Fetch the data
ocean_api_url = 'https://global-warming.org/api/ocean-warming-api'



# Check if the request was successful
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
    
    df.to_csv('ocean_data.csv', index=False)

    print("Data saved to climate_data.csv")
except requests.exceptions.RequestException as e:
    # Handle any exception that occurs during the request
    print(f"Failed to retrieve data: {e}")



