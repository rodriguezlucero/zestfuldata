import requests
import json

from Requests import Requests


# Author    : Lucero Rodriguez
# Date      : Wednesday November 25, 2020
# Assumption: Input used: "8 Potatoes, Onions, Carrot, 8lb Turkey, 12lb brisket, 1/2 cup bread crumbs"
# Purpose   : This file makes a call to the 'Zestful Data API', and then parses the returned json,
#             and inserts the parsed data in to the database

class RequestTest:
    __ZESTFUL_URL = "https://zestful.p.rapidapi.com/parseIngredients"

    def __init__(self):
        pass

    @staticmethod
    def __format_json(self, payload):
        text = json.dumps(payload, sort_keys=True, indent=4)
        print(text)

    def request_zestfuldata(self):
        url = self.__ZESTFUL_URL
        zestful_payload = "{\n    \"ingredients\": [\n        \"8 Potatoes\",\n        \"Onions\",\n        \"Carrot\",\n        \"8lb Turkey\",\n        \"12lb brisket\",\n        \"1/2 cup bread crumbs\"\n    ]\n}"
        headers = {
            'content-type': "application/json",
            'x-rapidapi-key': "85791eb068msha85aad63547a01ap108061jsncf3402c5e5f5",
            'x-rapidapi-host': "zestful.p.rapidapi.com"
        }

        response = requests.request("POST", url, data=zestful_payload, headers=headers)
        return json.loads(response.text)


# TEST: make the request, and insert returned data to db
request = RequestTest()
zestful_request = request.request_zestfuldata()

request_test = Requests()
request_test.insert_zestful_data(zestful_request)
