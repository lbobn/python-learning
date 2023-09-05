# 详细翻与反爬机制2

import urllib.request
import urllib.parse

url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/116.0.1938.69'
# }

# Cookie 反爬
# 起决定因素的Cookie
headers = {
    # 'Accept': '*/*',
    # # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Acs-Token': '1693904699640_1693904985942_HoMf0nVBoHa2d/Ebbe5tg6SzkG7q1iql6BfkfzKD27v6NLZhBKiu0w79dxUYyr3bwXaLoabmF83KCNk/BED2Rv+lzdBZyC1V8Pb0cf9rFrUAmBMrIE74bCESNA918RL/SPTeqI5dZ95D7iUuvUAFaOnMkfPaF+Y32mwZ+Rlm4dY6+aT7wPIphWX9LmhLyqsiKxH4+HU9wcJzlGRiV5XPDBjucNigEZ6xyZqbbU+7+oIzbVrH8dOvQ0ksIB0E3zAif4Nk2m4nsceZgIpc8KFJtsLBL0GKLlwit5M8IkZobvrRgYCS4PC0CCihc9EmLJMfzMFqGK2Yk/GgrMoMVwVLI02TP+R0dV5gTa0OuYhuQFylC4uPIy5f2jv42BfvCBMhMsFiGxl/5+nAcNOIfTFhkYts3lcMqZGhFQjbzzyfCzyx0/6h/ZZqLRcqlVP58j6dpYgSbjRWP9q7srYJtf9t0jHzK09zfi6gY5FLthIYxJQb0pRLatzwljVACTFd9bZmXS1/BWdleaW+Bt3ObMCHNg==',
    # 'Connection': 'keep-alive',
    # 'Content-Length': '149',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=349B3C1CF7A47DFAADBDCAB147325E9B; PSTM=1632752106; __yjs_duid=1_193e4db6ba368ee6ed3e182b4ad8e4771633013035608; BAIDU_WISE_UID=wapp_1671366971842_543; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; __bid_n=18862de40406096ece3202; BDUSS=Z1NDVGOXk1Z3VhdkYyazJTYy04dWhjWmJJajBTeC1Jb0Zla1luUmRVbzNPflJrSVFBQUFBJCQAAAAAAAAAAAEAAAB5QsJ-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADeuzGQ3rsxkd1; BDUSS_BFESS=Z1NDVGOXk1Z3VhdkYyazJTYy04dWhjWmJJajBTeC1Jb0Zla1luUmRVbzNPflJrSVFBQUFBJCQAAAAAAAAAAAEAAAB5QsJ-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADeuzGQ3rsxkd1; ZFY=A2:BwCtyfKeLx9mOFJMK5LHwnwWwfseg9YymkJVUWA2k:C; MCITY=-233%3A; RT="z=1&dm=baidu.com&si=f7f749de-df21-4402-8701-7a0cee848e21&ss=lm3i84o1&sl=7&tt=5c1&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=12z1&ul=19vq&hd=19vt"; BA_HECTOR=0h210h212ha0052la0a18l2f1ifbhns1p; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID=3B2E75386025F86FFA6CBA8AB8161EE2:SL=0:NR=10:FG=1; BAIDUID_BFESS=3B2E75386025F86FFA6CBA8AB8161EE2:SL=0:NR=10:FG=1; H_WISE_SIDS=216841_213349_214807_110085_244729_254835_261721_236312_256419_265615_265881_266368_259031_268570_268030_265986_259642_269400_256154_269731_268235_269749_269904_267066_256739_270335_270460_270603_270548_271170_271176_269771_267659_271319_270102_271562_270442_271873_270158_269876_271952_269627_234296_234208_269296_271188_270055_272278_267596_272613_253022_271689_272473_272821_272838_272802_260335_272987_272997_273066_267558_273090_273164_273119_273143_273245_273300_273400_273396_271158_273521_273197_271147_273670_273704_273317_264170_270185_273734_263619_263749_273902_273922_274081_273958_273965_274139_274152_269609_274209_273917_274238_273045_273593_274301_272806_203518_272333_272319_274385_272560_274426_274440_274766_274762_270141_274774_8000083_8000103_8000120_8000149_8000164_8000165_8000167_8000185_8000190; ET_WHITELIST=etwhitelistintwodays; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1693836515,1693903796; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1693903796; ab_sr=1.0.1_YTkwNDk3NTQ5NDUzOGJhYTM3ZjgwOGNiYjE4YjVkOGU2YjY2ZGQzYjEwYTM4OWJjNDViMWEzMTRiZTE2YmE1ZmU5NDI4NzBkYmQyNTc1NWI1MTYyYTQ4NDhhNzk1NTc4MGNiZmU1YjJmNDRhMDI3ODA0MjUyN2MzMmQ4N2E0NDA2ODIwMjhhMGRkNDczNGRkYmI4YjEwYjA0Mjg3ODUxMDIzZjcwYTEzMWIyODZkM2E1NGVmNmI5YjdhNTQ3MDRi',
    # 'Host': 'fanyi.baidu.com',
    # 'Origin': 'https://fanyi.baidu.com',
    # 'Referer': 'https://fanyi.baidu.com/',
    # 'Sec-Fetch-Dest': 'empty',
    # 'Sec-Fetch-Mode': 'cors',
    # 'Sec-Fetch-Site': 'same-origin',
    # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    # 'X-Requested-With': 'XMLHttpRequest',
    # 'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    # 'sec-ch-ua-mobile': '?0',
    # 'sec-ch-ua-platform': '"Windows"',
}

data = {
    "from": "en",
    "to": "zh",
    "query": "hello",
    "transtype": "realtime",
    "simple_means_flag": "3",
    "sign": "54706.276099",
    "token": "ce092e4e5500f45bc2cbec8638ef4027",
    "domain": "common",
    "ts": "1693904991793"
}

#
data = urllib.parse.urlencode(data).encode("utf-8")

request = urllib.request.Request(url, data, headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

import json

json_loads = json.loads(content)

print(json_loads)
