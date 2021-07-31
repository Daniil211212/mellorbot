import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

main_token = '67f3d7f2fecbcfb643397182811d26bf3942e01021a406f365f5126f5e32ff68e1c90da290e4ee9ed2756'

vk_session = vk_api.VkApi(token=main_token)
longpoll = VkLongPoll(vk_session)

def sender(id, text):
    vk_session.method('messages.send', {'chat_id': id, 'message' : text, 'random_id' : 0})
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.from_chat:
            msg = event.text.lower()
            id = event.chat_id
            if msg == "#pokex5":
                for i in range(5):
                    sender(id, "@all, @all, @all, @all, @all. Poke Машина запущена")
            if msg == "#status":
                sender(id, "Status: Online, Dev: @rodionovd21, если вылезло это сообщение - бот готов к работе.")
            if msg == "#pokex10":
                for i in range(10):
                    sender(id, "@all, @all, @all, @all, @all. Poke Машина запущена")
