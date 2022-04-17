import random
import json
from db.sql_req import get_response, write_new_phrase
from sqlalchemy.ext.asyncio.session import AsyncSession

async def reply_to_message(message_text: str, vk_api, user_id: int, session: AsyncSession):
    
    replies = await get_response(session, message_text)

    if message_text.find('/') != -1:
        st = message_text.split('/')
        await write_new_phrase(session, st[0], st[1])
        reply_text = "Я всё помню"
        vk_api.messages.send(
            user_id = user_id, 
            message = reply_text, 
            random_id = random.randint(0, 500000000000000000000000000),
            v=5.131
            )
        return True


    if len(replies) == 0:
        reply_text = "ЧЗХ"
        
        vk_api.messages.send(
            user_id = user_id, 
            message = reply_text, 
            random_id = random.randint(0, 500000000000000000000000000),
            v=5.131
            )
        reply_text = "Отправьте то-то"
        vk_api.messages.send(
            user_id = user_id, 
            message = reply_text, 
            random_id = random.randint(0, 500000000000000000000000000),
            v=5.131
            )
        #reply_text = "Если вы "
    
    for reply in replies:
        reply_text = reply.answer
        vk_api.messages.send(
            user_id = user_id, 
            message = reply_text, 
            random_id = random.randint(0, 500000000000000000000000000),
            v=5.131
            )

async def start(vk_api, user_id):
    message = "Привет, чтобы получать от меня уведомления выбери свою группу из предложенных вариантов"
    keyboard = {
        "one_time": True,
        "buttons": [
            [
                {
                    "action":{
                        "type": "text",
                        "payload": '{"command":"friends"}',
                        "label": "Друзья"
                    },
                    "color": "primary"
                },
                {
                    "action":{
                        "type": "text",
                        "payload": '{"command":"classmates"}',
                        "label": "Одноклассники"
                    },
                    "color": "primary"
                },
                {
                    "action":{
                        "type": "text",
                        "payload": '{"command":"programmers"}',
                        "label": "Программисты"
                    },
                    "color": "primary"
                },
            ]
        ]
    }
    vk_api.messages.send(
        user_id=user_id,
        message=message,
        keyboard=json.dumps(keyboard),
        random_id = random.randint(0, 500000000000000000000000000),
        v=5.131
    )