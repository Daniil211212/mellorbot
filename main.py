import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

main_token = '66789f57316dd90cd3714d0b4de68d3235214ca67637b69d7891d461bb66b382e7f645aae616edd2fdd5c'

vk_session = vk_api.VkApi(token=main_token)
longpoll = VkBotLongPoll(vk_session, 206197090)

def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message' : text, 'random_id' : 0})

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            id = event.chat_id
            msg = event.object.message['text'].lower()
            if msg == "test":
                sender(id, "testing...")