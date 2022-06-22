import datetime
import googleapiclient.discovery
import google.auth

# ①Google APIの準備をする
SCOPES = ['https://www.googleapis.com/auth/calendar']
# 研究用のGoogle Calendarを指定
calendar_id = '1e1fsosuuvssr0ctds7rnmk7q0@group.calendar.google.com'
# Googleの認証情報をファイルから読み込む
gapi_creds = google.auth.load_credentials_from_file('decoded-keel-350601-42b1cb0b7313.json', SCOPES)[0]
# APIと対話するためのResourceオブジェクトを構築する
service = googleapiclient.discovery.build('calendar', 'v3', credentials=gapi_creds)


# ②Googleカレンダーからイベントを取得する
# 現在時刻を世界協定時刻（UTC）のISOフォーマットで取得する
now = datetime.datetime.utcnow().isoformat() + 'Z'
check = now[:10]
event_list = service.events().list(
     calendarId=calendar_id, timeMin=now,
     maxResults=10, singleEvents=True,
     orderBy='startTime').execute()


# ③イベントの開始時刻、終了時刻、概要，場所を取得する
# 今日の日付と等しい予定のみを取得するようにする．
events = event_list.get('items', [])
count = 0
for event in events:
    if event["start"].get('dateTime', event['start'].get('date'))[:10] == check:
        # print(event["start"].get('dateTime', event['start'].get('date'))[11:16])
        count += 1

formatted_events = [[event['start'].get('dateTime', event['start'].get('date')), # start time or day
     event['end'].get('dateTime', event['end'].get('date')), # end time or day
     event['summary']] for event in events]

for i,event in enumerate(events):
    if "location" in event:
        formatted_events[i].append(event["location"])
    else:
        formatted_events[i].append(" ")

print(formatted_events[:count])

