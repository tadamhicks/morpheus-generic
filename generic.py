import requests
import argparse


def call_get_api(url, token):
    auth_header = {"Authorization": "Bearer " + token}
    auth_header["Content-Type"] = "application/json"
    json_data = requests.get(url, headers=auth_headers, verify=false).json()
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
    
    response = call_get_api(parsed.url, parsed.token)
    
    print str(response)