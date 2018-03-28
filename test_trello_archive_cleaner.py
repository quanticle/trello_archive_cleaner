import unittest
import requests
from trello_archive_cleaner import TrelloRestClient, AuthInfo, Board

class LiveTests(unittest.TestCase):

    def testGetBoards(self):
        members_url = "https://api.trello.com/1/members/rohitpatnaik?key={api_key}&token={oauth_token}"
        auth_info = AuthInfo()
        auth_info.read_from_file("api_keys.json")
        print("Sending request to: {}".format(members_url.format(api_key=auth_info.api_key, oauth_token=auth_info.oauth_token)))
        member_info_response = requests.get(members_url.format(api_key=auth_info.api_key, oauth_token=auth_info.oauth_token))
        self.assertEqual(member_info_response.status_code, 200)
        boards_url = "https://api.trello.com/1/members/rohitpatnaik/boards?key={api_key}&token={oauth_token}"
        print("Sending request to {}".format(boards_url.format(api_key=auth_info.api_key, oauth_token=auth_info.oauth_token)))
        boards_response = requests.get(boards_url.format(api_key=auth_info.api_key, oauth_token=auth_info.oauth_token))
        self.assertEqual(boards_response.status_code, 200)
        boards = boards_response.json()
        print(boards)
        

if __name__ == '__main__':
    unittest.main()
