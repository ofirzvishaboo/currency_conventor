import requests


def get_data():
    url = 'https://api.exchangerate.host/latest'
    response = requests.get(url)
    data = response.json()


    # Get the request data as a dictionary
    # response1 = requests.get(url)
    # data = response1.json()

    # Extract the image title, url and, explanation
    shekel1 = data["rates"]["ILS"]
    # todays_date = data["date"] if wanted
    dollar1 = data["rates"]["USD"]
    dollar = shekel1 / dollar1  # Calculating from eur base for use
    shekel = dollar1/shekel1  # Calculating from eur base for use
    eur = shekel1 / 1  # Calculating from eur base for use
    return dollar, eur, shekel


get_data()
