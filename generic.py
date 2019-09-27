import requests
import argparse


def call_api(url, token):
    auth_header = {"Authorization": "Bearer " + token}
    auth_header["Content-Type"] = "application/json"
    json_data = requests.post(url, headers=headers, json=query, verify=verify).json()
    return json_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Morpheus info')

    parser.add_argument(
        '-t',
        '--token',
        default='administrator',
        help='provide a Morpheus API Token'
    )

    parser.add_argument(
        '-u',
        '--url',
        default='https://morpheus.com',
        help='provide a Morpheus API URL'
    )


    parsed = parser.parse_args()
    username = parsed.username
    
    response = call_api(parsed.token, parsed.url)
    
    print str(response)