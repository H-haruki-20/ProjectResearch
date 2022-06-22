Google Calendarに登録された予定(行き先と時刻)から，その地点における天気予報の情報を取得し，どこかしらで雨が降る可能性が高い場合に傘立てに取り付けたテープ LEDが点灯するIoT機器を作成しています．

まだ完成はしていないのですが，現在Google Calendar APIとopenweather APIを利用して，雨が降る予報のときは1つのLEDを点灯させるところまでできました．これからテープLEDなどを用いて雨の表現を考えていきます．

idea.pdf : 制作している作品の概要と完成予定図
sample.py : Google Calendarからその日中の予定を取得．
openweather.py : openweatherAPIを叩く．(郵便番号から天気予報を取得)
		ラズパイ上でGPIOピンに電流を流すかどうかの制御

app.py : LINE botで予定を通知，または傘が必要か否かの通知．
