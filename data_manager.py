from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/0b454e5fe21e86cfcf0bdab83e13b8bd/benFlightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
      customers_endpoint = "https://api.sheety.co/0b454e5fe21e86cfcf0bdab83e13b8bd/benFlightDeals/users"
      response = requests.get(url=customers_endpoint)
      data = response.json()
      self.customer_data = data["users"]
      return self.customer_data