import json
import requests


def get_api():
    """ Retrieve the most starred Python repos from Github API. """
    url = 'https://api.github.com/search/repositories?q=language:Python&sort=stars&order=desc'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url)
    assert response.status_code == 200
    datum = response.text
    data = json.loads(datum)
    data_list = data['items']

    return data_list
