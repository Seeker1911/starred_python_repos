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

def format_json_to_dicts(results):
    data = [{'repo_id':r.get('id'),
                        'name':r.get('name'),
                        'url':r.get('html_url'),
                        'created_date':r.get('created_at'),
                        'last_push_date':r.get('pushed_at'),
                        'description':r.get('description'),
                        'stars':r.get('watchers'),
                        'avatar':r.get('owner',{}).get('avatar_url')} for r in results]

    return data
