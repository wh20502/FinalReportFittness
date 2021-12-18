from urllib.parse import parse_qsl, parse_qs
import datetime
from line_chatbot_api import *

def call_service(event):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            # thumbnail_image_url=url_for('static', filename='images/brown_1024.jpg', _external=True),
            thumbnail_image_url='https://mirtomo.com/wp-content/uploads/2019/08/9_4.jpg',
            title='請問想要知道什麼設施的介紹呢?',
            text='請在下方點選您想知道的項目',
            actions=[
                MessageAction(
                    label='臥姿彎腿機',
                    text='我想知道臥姿彎腿機怎麼用'
                ),
                MessageAction(
                    label='背伸機',
                    text='我想知道背伸機怎麼用'
                ),
                MessageAction(
                    label='大腿推蹬機',
                    text='我想知道大腿推蹬機怎麼用'
                ),
                MessageAction(
                    label='多功能單/雙槓輔助機',
                    text='我想知道多功能單/雙槓輔助機怎麼用'
                ),
                MessageAction(
                    label='腿內收機',
                    text='我想知道腿內收機怎麼用'
                ),
                MessageAction(
                    label='腿外展機',
                    text='我想知道沝外展機怎麼用'
                ),
                MessageAction(
                    label='三頭訓練機',
                    text='我想知道三頭訓練機怎麼用'
                ),
                MessageAction(
                    label='腹部旋轉機',
                    text='我想知道腹部旋轉機怎麼用'
                ),
                MessageAction(
                    label='腹部前驅訓練機',
                    text='我想知道腹部前驅訓練機怎麼用'
                ),
                MessageAction(
                    label='二頭訓練機',
                    text='我想知道二頭訓練機怎麼用'
                ),
                MessageAction(
                    label='腿部伸張機',
                    text='我想知道腿部伸張機怎麼用'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token, message)