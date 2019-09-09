# �C���|�[�g���郉�C�u����
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

# �y�ʂȃE�F�u�A�v���P�[�V�����t���[�����[�N:Flask
app = Flask(__name__)


#���ϐ�����LINE Access Token��ݒ�
LINE_CHANNEL_ACCESS_TOKEN = os.environ[8mVYpp/SacL0hTRM41ZCK8gKaeeGjI8zSilyEqvzACeGL9MrPANr+zdg/NvRlPDuNPzTtti41CYXYHvR76B/Ii5MhRpMBRupGf14yYdaO5hdZoY20JRzxOVTLPmj2aTqWcLTGJDC/Wvq1qsGU0be5gdB04t89/1O/w1cDnyilFU=]
#���ϐ�����LINE Channel Secret��ݒ�
LINE_CHANNEL_SECRET = os.environ[2ccda15a8da557a79b65c524bad77dd8
]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

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

# MessageEvent
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='�u' + event.message.text + '�v���ĉ��H')
     )

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)