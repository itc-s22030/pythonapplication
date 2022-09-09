
# 取得先URL
# https://weather.tsukumijima.net/

import string
import requests
import json
#-------------------------------
#初期設定
#-------------------------------
#JSONファイルより都道府県の都市名とAPI取得番号（ID）データを取得する
json_open = open("weatherForecast.json", 'r', encoding="utf-8")
json_load = json.load(json_open)

while True:
    try:
        input_data = input()

        if input_data != "exit":

            for json_dt in json_load["weather"]:

                strDisp = json_dt["cyit_Name"] + "\n"

                if json_dt["cyit_Key"] == input_data:

                    for id in json_dt["data_id"]:

                        strDisp += id["title"] + "\n"
                        
                        url = "https://weather.tsukumijima.net/api/forecast/city/" + id["id"]
                        weather_json = requests.get(url)
                        weather_data = weather_json.json()

                        #天気情報を出力変数にセット
                        for jsonObj2 in weather_data["forecasts"]:
                            strDisp += "\t" + jsonObj2["dateLabel"]
                            strDisp += "\t" + jsonObj2["telop"] + "\n"

                            print(strDisp)
        else:
            break
    except:
        print("天気情報取得失敗しました。")
        break

