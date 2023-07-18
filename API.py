import requests


def get_data():
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()


    # Get the request data as a dictionary

    # Extract the conversion rates
    shekel1 = data["rates"]["ILS"]
    dollar1 = data["rates"]["USD"]

    # Calculations for the use
    dollar = shekel1 / dollar1
    shekel = dollar1/shekel1
    eur = shekel1 / 1
    return dollar, eur, shekel  # Returns values


get_data()
