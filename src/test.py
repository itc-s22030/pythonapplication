import requests
import sys
import json

postal = input("郵便番号を入力してください : ")
url = f"http://zipcloud.ibsnet.co.jp/api/search?zipcode={postal}"
address = ""
kana = ""
response = requests.get(url)
json_result = response.text
json_toresult = json.loads(response.text)

if json_toresult["message"] == None:
    result_dic = json_toresult["results"][0]
else:
    print("検索不可")
    sys.exit()

for n in range(1, 4):
    address += result_dic["address" + str(n)]
    kana += result_dic["kana" + str(n)]

context = {"郵便番号:": postal, "カナ:": kana, "住所:": address}

for x, y in context.items():
    print(x, y)