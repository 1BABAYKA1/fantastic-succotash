import unittest
from unittest.mock import Mock, patch
import requests


class TestAPIRequest(unittest.TestCase):


    def test_api_request(self):
        mytoken = 'ppo_10_15261'
        day = '04'
        month = '03'
        year = '23'
        url = f"https://dt.miet.ru/ppo_it_final?day={day}&month={month}&year={year}"
        headers = {"X-Auth-Token": mytoken}

        response_json = {
            "message": {
                "windows": {
                    "data": "test_data"
                }
            }
        }

        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = response_json

        response = requests.get(url, headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message']['windows']['data'], 'test_data')
        self.assertFalse(mock_get.return_value.json.called)

if __name__ == '__main__':
    unittest.main()
