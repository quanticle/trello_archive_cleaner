import requests
import json

class AuthInfo:
    
    def __init__(self, api_key=None, oauth_token=None):
        self.api_key = api_key
        self.oauth_token = oauth_token

    def read_from_file(self, filename):
        with open(filename, 'r') as auth_handle:
            auth_json = json.load(auth_handle)
            self.api_key = auth_json["api_key"]
            self.oauth_token = auth_json["oauth_token"]

class Board:
    def __init__(self, board_id, name):
        self.board_id = board_id
        self.name = name

class TrelloRestClient:

    def __init__(self, auth_info):
        self.auth_info = auth_info

    def get_boards(self):
        request_url = "https://api.trello.com/1/boards?fields=name,url&key={api_key}&token={oauth_token}".format(self.auth_info.api_key, self.auth_info.oauth_token)
        boards_list_request = requests.get(request_url)
        boards_json = boards_list_request.json()
        return boards_json
