def locale():
    import requests
    import json
    res = requests.get(url='https://ipgeolocation.com')
    results = {}
    data = json.loads(res)
    results['ip'] = data['ip']
    results['coords'] = data['coords']
    return results
