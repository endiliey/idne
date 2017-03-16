import requests
import json
import robobrowser

def get_latest_verdict(user):
    r = requests.get('http://codeforces.com/api/user.status?' +
                     'handle={}&from=1&count=1'.format(user))
    js = r.json()
    if 'status' not in js or js['status'] != 'OK':
        raise ConnectionError('Cannot connect to codeforces!')
    result = js['result'][0]
    id_, verdict = result['id'], result['verdict']
    return id_, verdict

a, b = get_latest_verdict('endijr')

print a
print b

