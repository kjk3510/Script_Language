# -*- coding: utf-8 -*-


import simplejson, urllib.request, urllib.parse, urllib.error

apikey = "fc19ad4f9ec307adb8af294d92874d69"
SEARCH_BASE ="http://apis.daum.net/search/knowledge"

def search(query, **args):
    args.update({
            'apikey': apikey,
            'q': query,
            'output': 'json'
    })

    #호출할 url을 만든다
    url = SEARCH_BASE + 'http://localhost' + urllib.parse.urlencode(args)

    #json으로 응답을 받는다.
    result = simplejson.load(urllib.request.urlopen(url))

    return result['channel']

info = search('OpenAPI')
for item in info['item']:
    print(item['title'])