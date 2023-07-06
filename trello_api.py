import requests
import os
import json
import pprint
import requests

class TrelloAPI:
    def __init__(self, token, key, secret):
        self.token = token
        self.key = key
        self.secret = secret
        self.base_url = "https://api.trello.com/1"


    def test_create_card(self, id_list):
        url = f"{self.base_url}/cards"
        query = {
            "idList": id_list,
            "key": self.key,
            "token": self.token,
        }

        response = requests.post(url, params=query)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            print(response.text)
            return False

    def get_boards(self):
        url = f"{self.base_url}/members/me/boards"
        query = {
            "key": self.key,
            "token": self.token
        }

        response = requests.get(url, params=query)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def get_lists(self, board_id):
        url = f"{self.base_url}/boards/{board_id}/lists"
        query = {
            "key": self.key,
            "token": self.token
        }

        response = requests.get(url, params=query)
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def get_board(self, board_id):
        url = f"{self.base_url}/boards/{board_id}"
        headers = {
            "Accept": "application/json"
        }
        query = {
            "key": self.key,
            "token": self.token
        }

        response = requests.get(url, headers=headers, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            print(response.text)
            return False

    def update_board_description(self, board_id, description):
        url = f"{self.base_url}/boards/{board_id}"
        query = {
            "key": self.key,
            "token": self.token,
            "desc": description
        }

        response = requests.put(url, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            print(response.text)
            return False

    def update_card_description(self, card_id, description):
        url = f"{self.base_url}/cards/{card_id}"

        query = {
            "key": self.key,
            "token": self.token,
            "desc": description
        }

        response = requests.put(url, params=query)
        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            print(response.text)
            return False

    def get_organization(self, org_id):
        url = f"{self.base_url}/organizations/{org_id}"
        query = {
            "key": self.key,
            "token": self.token
        }
        response = requests.get(url, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            return False

    def get_cards(self, board_id):
        url = f"{self.base_url}/boards/{board_id}/cards"
        query = {
            "key": self.key,
            "token": self.token
        }
        response = requests.get(url, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            print(response.status_code)
            print(response.text)
            return False

    def create_card(self, list_id, name, desc):
        url = f"{self.base_url}/cards/"

        headers = {
                "Accept": "application/json"
        }
        query = {
            "idList": list_id,
            "key": self.key,
            "token": self.token,
            "name": name,
            "desc": desc
        }

        response = requests.post(url, headers=headers, params=query)

        if response.status_code == 200:
            print(response)
            return True
        else:
            print(response.status_code)
            print(response.text)
            return False

    def create_board(self):
        url = f"{self.base_url}/boards/"
        query = {
            "name": "Test Board",
            "key": self.key,
            "token": self.token
        }
        response = requests.post(url, params=query)
        return response.json()
