from dotmap import DotMap
import logging, requests
import json


def get_user(req):
    try:
        res = requests.get('http://localhost:8000/account/whoami/', headers={'Authorization': req.headers.get('Authorization')})
        if res.status_code != 200:
            logging.error(res.status_code)
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
            print(res.status_code)
            raise
        return DotMap(res.json())
    except:
        logging.error('Invalid token')
    return None

