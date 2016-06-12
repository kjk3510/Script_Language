# -*- coding: utf-8 -*-


from urllib.request import urlopen, Request
from urllib.parse import urlencode, quote_plus

url = 'http://openapi.sejong.go.kr/openapi-data/service/PublicBikeData/getPublicBikeStationList'

svkey = 'PTAX4yzA4NS2ah0wIAKmx5KV%2Fn9NY47bPPOLr%2FZL4qYR2svXwwutj%2B8BrWO%2F6x2KwzeXZ73L9tzUmGwYCqh3Xg%3D%3D'
svkey = svkey.encode('utf-8')
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : svkey
                                  , quote_plus('numOfRows') : '999', quote_plus('pageNo') : '1' })

rq = Request(url + queryParams)
rq.get_method = lambda: 'GET'
response_body = urlopen(rq).read()
print(response_body)