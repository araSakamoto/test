from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    FollowEvent, MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
import os

app = Flask(__name__)

#環境変数取得(LINE DEVELOPPER)
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["8mVYpp/SacL0hTRM41ZCK8gKaeeGjI8zSilyEqvzACeGL9MrPANr+zdg/NvRlPDuNPzTtti41CYXYHvR76B/Ii5MhRpMBRupGf14yYdaO5hdZoY20JRzxOVTLPmj2aTqWcLTGJDC/Wvq1qsGU0be5gdB04t89/1O/w1cDnyilFU="]
YOUR_CHANNEL_SECRET = os.environ["2ccda15a8da557a79b65c524bad77dd8"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

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
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
