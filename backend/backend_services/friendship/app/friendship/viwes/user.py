import requests, json, logging
from dotmap import DotMap


def get_user(req, user_id:int = None):
    try:
        if not user_id:
            res = requests.get('http://localhost:8000/account/whoami/', headers={'Authorization': req.headers.get('Authorization')})
        else:
            res = requests.get(f'http://localhost:8000/account/{user_id}', headers={'Authorization': req.headers.get('Authorization')})
        if res.status_code != 200:
            raise
        return DotMap(res.json())
    except:
        logging.error('Invalid token')
    return None


def save_user(req, user: DotMap):
    user = json.dumps(user.toDict())
    try:
        res = requests.patch(
            'http://localhost:8000/account/update-profile/', 
            user,
            headers={'Authorization': req.headers.get('Authorization')})
        if res.status_code != 200:
            raise
        return res.json()
    except:
        logging.error('Invalid token')
    return None