# openweathermap APIを利用する．

import requests
import json
import sample
import re

API_TOKEN = "9a611863b603cfa5de88c8304076fa5d"
weather = []
if __name__ == "__main__":
    count = sample.count
    for i in range(count):
        result = re.search(r"\d{3}\-\d{4}", sample.formatted_events[:count][i][3])
        ZIPCODE = result.group()

        response = requests.get(
            "https://api.openweathermap.org/data/2.5/forecast",
            params={
                ## 緯度・軽度を指定する場合
                # "lat": "35.68944",
                # "lon": "139.69167",

                ## 都市名で取得する場合
                # "q": "tokyo",
                "zip" : ZIPCODE + ",jp",

                "appid": API_TOKEN,
                "units": "metric",
                "lang": "ja",
                "cnt" : "7",
            },
        )
        ret = json.loads(response.text)
        start = int(sample.formatted_events[:count][i][0][11:13])
        try:
            print(ret["list"][start//3]["weather"][0]["main"])
            weather.append(ret["list"][start//3]["weather"][0]["main"])
        except KeyError:
            print("KeyError (No match with OpenWeatherAPI)")

