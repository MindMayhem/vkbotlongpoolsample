import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

token = 'ec00fcadeafd2757341651684a5e2fdbc2a419109a5975a79eda657b065f63d386758ff68c6026feeca7e'
vk = vk_api.VkApi(token=token)
vk._auth_token()

print(  # Получаем информацию о чате.
        vk.method('messages.getConversations')
    )
def start(message,name,color_but):
    keyboard = VkKeyboard(one_time=False) # Инилициализация клавиатуры

    keyboard.add_button(name, color=color_but) # Cобсна сама клавиша



    vk.method('messages.send',
              {'chat_id': 1,
               'message': message,
               'keyboard': keyboard.get_keyboard() # Отправка клавиатуры вслед за сообщением (точно так же как и в телеге)
               })
def write_msg(message):
    vk.method('messages.send', {'chat_id': 1, 'message': message})


def main(): # Работа с сообщениями

    longpoll = VkBotLongPoll(vk, 169452609)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print('Новое сообщение:')
            print('Для меня от: {}'.format(event.obj.from_id))
            print('Текст:', event.obj.text)
            if event.obj.text == "Шалом":
                print('Клавиатура появилась')
                start("Всем шалом!","Definetively Not Button",VkKeyboardColor.NEGATIVE)
            elif event.obj.text == "[club169452609|@something_tasty] Definetively Not Button":
                write_msg("Теперь я буду жить тут вечно")
                print("Сообщение вроде как отправилось :/")
            elif event.obj.text == "[club169452609|@something_tasty] Definetively Button":
                write_msg("Не, я лентяй :Р")
                print("Сообщение вроде как отправилось :/")
            elif event.obj.text == "Давай другую":
                print('Клавиатура появилась')
                start("А теперь тут я!","Definetively Button",VkKeyboardColor.POSITIVE)
            elif event.obj.text == "Сворачиваемся":
                keyboard = VkKeyboard(one_time=False)
                vk.method('messages.send',
                          {'chat_id': 1,
                           'message': "Ладно, мы пойдем уже",
                           'keyboard': keyboard.get_empty_keyboard()
                           })

        else:
            print(event.type)
            print()


if __name__ == '__main__':
    main()