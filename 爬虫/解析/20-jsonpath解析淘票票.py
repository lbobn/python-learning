"""
需求：获取所有城市
"""

import urllib.request
import json
import jsonpath

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1694334153059_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'Cookie': 'cna=AMDYGTSXBBsCAW8Sj9Z4kSkO; enc=AX12IPxOd0LPAAAAAHuK6VMB%2FXow%2FWv9ZTz9R%2F1C%2FQFz7Dw4r7qHuLFyKdRvpakbQxxEL2a1o55OEBI40x%2BKs7U%3D; t=ad0a1d1554e08ca2c0dfbd1f3a32ef72; xlly_s=1; cookie2=1f7b2c06d8a33827c82151b8be8a316a; v=0; _tb_token_=fbe58eb831164; tfstk=dJeBF6VwNeYIkyr7bQsaG38903H5by62P3i8mupe2vHKVTaz7HrU4JPs2zzGqMDU24a77V4SZM0ry4az2WSN3tr3xYD-PZWV3zaMpv1YdCHwnNkoeZ72_LhhhY4A__JVf2IA8OGP5qv7K0DwFIf37Lp8pTcIlduijcw1IX04vRpRQOpql_x6NhGDFcgVfGOkZTnSqO1..; l=fBEeWjOcgAeYxIdvBO5Blurza77t2IObzPVzaNbMiIEGa1oC9FOCsNC6Rs4WWdtjgT5v_etyVhmX9d3JyRUU-NsWHpfuKtyuJdpwReM3N7AN.; isg=BIKCe60iUqAWP0sWRsB57xZM04jkU4ZtoFl0Osyak_WgHyCZtOcdfLZRzxtjSv4F',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Referer': 'https://dianying.taobao.com/',
}

request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
content: str = response.read().decode('utf-8')
# 获取到的json字符串不合规
json_content = content.split('(')[1].split(')')[0]

json = json.loads(json_content)
city_list = jsonpath.jsonpath(json, '$..regionName')

print(city_list)
