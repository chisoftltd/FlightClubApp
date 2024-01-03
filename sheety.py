import os

import requests

BEARER = os.getenv("API_BEARER_SHEETY_REPL.IT")
USERNAME = os.getenv("0b454e5fe21e86cfcf0bdab83e13b8bd")

PROJECT = "benFlightDeals"
SHEET = "users"

base_url = "https://api.sheety.co"


def post_new_row(first_name, last_name, email):
  #endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
  #url = base_url + endpoint_url
  url = "https://api.sheety.co/0b454e5fe21e86cfcf0bdab83e13b8bd/benFlightDeals/users"

  headers = {
      "Authorization": f"Bearer {BEARER}",
      "Content-Type": "application/json",
  }

  body = {
      "user": {
          "firstName": first_name,
          "lastName": last_name,
          "email": email,
      }
  }

  response = requests.post(url=url, headers=headers, json=body)
  response.raise_for_status()
  print(response.text)
