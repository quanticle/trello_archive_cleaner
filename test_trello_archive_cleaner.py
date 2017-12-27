import unittest
import requests
from trello_archive_cleaner import TrelloRestClient, AuthInfo, Board

class LiveTests(unittest.TestCase):

    def testGetBoards(self):
        boards_url = "https://api.trello.com/1/boards?fields=name,url&key={api_key}&token={oauth_token}"
        auth_info = AuthInfo()
        auth_info.read_from_file("api_keys.json")
        print("Sending request to: {}".format(boards_url.format(api_key=auth_info.api_key, oauth_token=auth_info.oauth_token)))
        board_response = requests.get(boards_url.format(api_key=auth_info.api_key, oauth_token=auth_info.oauth_token))
        self.assertEqual(board_response.status_code, 200)
        

if __name__ == '__main__':
    unittest.main()
