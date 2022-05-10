from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/f4df2eb9ba37cf1a01eecb0ddc650e3f/flightDealsForJoshpy/prices"
SHEETY_USER_ENDPOINT = "https://api.sheety.co/f4df2eb9ba37cf1a01eecb0ddc650e3f/flightDealsForJoshpy/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.users = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def give_user_data(self, first, last, email):
        # response = requests.get(url=SHEETY_USER_ENDPOINT)
        # data = response.json()
        # self.users = data["users"]
        #
        body = {
            "user": {
                "firstName": first,
                "lastName": last,
                "email": email
            }
        }
        response = requests.put(url=f"{SHEETY_USER_ENDPOINT}/{2}", json=body)
        print(response.text)

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
