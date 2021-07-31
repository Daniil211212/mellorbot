import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

main_token = '67f3d7f2fecbcfb643397182811d26bf3942e01021a406f365f5126f5e32ff68e1c90da290e4ee9ed2756'

vk_session = vk_api.VkApi(token=main_token)
longpoll = VkBotLongPoll(vk_session)

def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message' : text, 'random_id' : 0})

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.from_chat:
            id = event.chat_id
            msg = event.object.message['text'].lower()
            if msg == "test":
                sender(id, "testing...")
