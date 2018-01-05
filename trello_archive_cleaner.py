import requests
import json

class TrelloRestClient:

    def send_get(self, url, params={}):
        get_response = requests.get(url, params=params)
        return get_response

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

class BoardGetter:
    def __init__(self, rest_client, auth_info):
        self.rest_client = rest_client
        self.auth_info = auth_info

    def get_boards(self, username):
        board_base_url = "https://api.trello.com/1/members/{username}/boards".format(username=username)
        board_list_params = {
            "fields": "id,name",
            "key": self.auth_info.api_key,
            "token": self.auth_info.oauth_token
        }
        get_boards_response = self.rest_client.send_get(board_base_url, params=board_list_params)
        if get_boards_response.status_code != 200:
            raise Exception("Received status code: {}".format(str(get_boards_response.status_code)))
        boards_json = get_boards_response.json()
        boards = []
        for board_json in boards_json:
            boards.append(Board(board_json["id"], board_json["name"]))
        return boards
            
        
        
