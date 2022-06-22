from flask import Flask, request, abort
import time,datetime
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

import sample

app = Flask(__name__)

line_bot_api = LineBotApi('cmxaIkBbfTJ70lFIb1BKyATtCW/8jdI5V4Gi7LEGvMsKbSii5TgstCZp8aFXit+FGJjUVKlIl6D82xJnJelYASxxfoz8yLSPyx50fgsdrtz2gYTier//WUPEg5LITXnfvKVSDv6FZg+Yl9P2Oao05gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7a4d0888fd79fe03be2aa52f9ee38215')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'




@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    lineRes = event.message.text
    if lineRes == "教えて":
        botRes = "今日の予定をお知らせします"
        time.sleep(10)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=botRes))


if __name__ == "__main__":
    app.run()