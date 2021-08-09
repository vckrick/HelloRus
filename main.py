from threading import Event
import vk_api
from vk_api.utils import get_random_id
import random

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

vk_session = vk_api.VkApi(token="")

longpoll = VkBotLongPoll(vk_session, "")

vk = vk_session.get_api()

while True:
    for event in longpoll.listen():
        print(event.object)
        if event.type == VkBotEventType.MESSAGE_NEW and event.message != "":
            vk.messages.send(user_id=event.message.from_id, peer_id=event.message.peer_id, random_id=get_random_id(), message="привет")
