import pandas as pd
import requests


url = 'https://www.binance.com/api/v3/ticker/24hr'


response = requests.get(api_url)


if response.status_code == 200:

    data = response.json()
    df = pd.DataFrame(data)


    df.to_csv('cobtask1.csv', index=False)

    print("Your CSV dataset has been created successfully.")
else:
    print("Unable to create CSV file. Check your data)