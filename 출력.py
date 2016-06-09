# -*- coding: utf-8 -*-


from urllib.request import Request, urlopen
from urllib.request import quote,

url = 'http://openapi.sejong.go.kr/openapi-data/service/PublicBikeData/getPublicBikeStationCount'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'PTAX4yzA4NS2ah0wIAKmx5KV%2Fn9NY47bPPOLr%2FZL4qYR2svXwwutj%2B8BrWO%2F6x2KwzeXZ73L9tzUmGwYCqh3Xg%3D%3D', quote_plus('numOfRows') : '999', quote_plus('pageNo') : '1' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body