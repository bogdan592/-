import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard  # <===
key = "4f25bd524a39012880a89cdab4bcb82108c17a38fd9bd191e78bc4b30f47c1bb01a139ecb0b0cdcb6f72b"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message, keyboard = None):  # <===
                from random import randint
                vk.method('messages.send',
                          {'user_id': user_id,
                           'random_id':randint(1,1000) ,
                           'message': message,
                           'keyboard':keyboard.get_keyboard() if keyboard else None,}  # <===
                          )

start_keyboard = VkKeyboard(one_time = True)  # <===
start_keyboard.add_button('START')

main_keyboard = VkKeyboard(one_time = True)  # <===

main_keyboard.add_button('Об авторе')
main_keyboard.add_button('Сделать пожертвование')
main_keyboard.add_line()
main_keyboard.add_button('Поиграться')
main_keyboard.add_button('Назад')


game_keyboard = VkKeyboard(one_time = True)

game_keyboard.add_button('Бумага')
game_keyboard.add_line()
game_keyboard.add_button('Ножницы')
game_keyboard.add_line()
game_keyboard.add_button('Камень')
game_keyboard.add_line()
game_keyboard.add_button('Назад.')

gamer_keyboard = VkKeyboard(one_time = True)
gamer_keyboard.add_button('Угадай число')
gamer_keyboard.add_line()
gamer_keyboard.add_button('Сыграть в камень ножницы бумага')
gamer_keyboard.add_line()
gamer_keyboard.add_button('Фортуна')
gamer_keyboard.add_line()
gamer_keyboard.add_button('Назад!')

fortun_keyboard = VkKeyboard(one_time = True)
fortun_keyboard.add_button('Правила')
fortun_keyboard.add_line()
fortun_keyboard.add_button('Начать игру')
fortun_keyboard.add_line()
fortun_keyboard.add_button('Назад.')

fortunka_keyboard = VkKeyboard(one_time = True)
fortunka_keyboard.add_button('Испытать удачу!')
fortunka_keyboard.add_line()
fortunka_keyboard.add_button('Назад.')


back_keyboard = VkKeyboard(one_time = True)
back_keyboard.add_button('Назад')
gamers={}
# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            print(text)
            if user_id in gamers:
                try:
                    otvet = int(text)
                except:
                    send_message(user_id,"Тут надо цифру а не букву ")
                    continue
                goal = gamers[user_id]['goal']
                if gamers[user_id]['lives'] < 1:              
                      send_message(user_id,"Проигрышь,жизни кончились ಥ_ಥ", main_keyboard)
                      del gamers[user_id]
                                     
                elif otvet > goal:                      
                    send_message(user_id,"Много")
                    gamers[user_id]['lives'] -= 1
                elif otvet < goal:
                    send_message(user_id,"Мало")
                    gamers[user_id]['lives'] -= 1
                else:
                    send_message(user_id,"Победа!!! 🥳", main_keyboard)
                    del gamers[user_id]
            
            else:                    
                if text == 'START'.lower():   
                      send_message(user_id,"Добро пожаловать",main_keyboard)  # <===
                elif text == 'Об авторе'.lower():   
                       send_message(user_id,"Bogdan",back_keyboard)
                elif text == 'Сделать пожертвование'.lower():   
                       send_message(user_id,"Укажи номер и пароль своей карты и я спишу с неё все деньги",back_keyboard)
                elif text == 'Угадай число'.lower():
                    from random import randint
                    gamers[user_id] = {'goal' : randint(1,8196),
                                       'lives': 15}
                    send_message(user_id,"Угадывай число от 1 до 8196 🤔. Утебя 15 попыток!😏")
                if text == 'узнать погоду'.lower():   
                    send_message(user_id,"ясно",back_keyboard)
                elif text == 'Сыграть в камень ножницы бумага'.lower():   
                    send_message(user_id,"У тебя нет шансов выйграть,но поиграй если хочешь",game_keyboard)
                elif text == 'Назад'.lower():   
                    send_message(user_id,"Хорошо",start_keyboard)
                elif text == 'Камень'.lower():   
                    send_message(user_id,"Бумага.Ты проиграл(а) 😭!",game_keyboard)
                elif text == 'Ножницы'.lower():   
                    send_message(user_id,"Камень.Ты проиграл(а) 😭!",game_keyboard)     
                elif text == 'Бумага'.lower():   
                    send_message(user_id,"Ножницы.Ты проиграл(а) 😭!",game_keyboard)
                elif text == 'Назад.'.lower():
                    send_message(user_id,"Хорошо",gamer_keyboard)
                elif text == 'Назад!'.lower():
                    send_message(user_id,"Хорошо",main_keyboard)
                elif text == 'Поиграться'.lower():                    
                    send_message(user_id,"Выбирай игру",gamer_keyboard)
                elif text == 'Фортуна'.lower():                    
                    send_message(user_id,"Бланодаря этой игре ты можешь разбогатеть",fortun_keyboard)              
                elif text == 'Правила'.lower():                    
                    send_message(user_id,"В этой игре есть единственная кнопка:Разбогатеть.Шанс выйграть 50/50.Если ты проиграешь то все заработанные деньги сгорят,так что не увлекайся!Удачи!!!",fortun_keyboard)
                elif text == 'Начать игру'.lower():                    
                    send_message(user_id,"Все деньги в твоих руках!",fortunka_keyboard)
                elif text == 'Испытать удачу!'.lower():                     
                    player = gamers[user_id]['number']
                    player = gamers[user_id]['player']
                    from random import randint
                    gamers[user_id] = {'number' : 2,
                                       'player': randint(1,3)}
                elif number > player:                      
                    send_message(user_id,"❌К сожалению ты проиграл❌")
        
                elif number < player:
                    send_message(user_id,"❌К сожалению ты проиграл❌")
                    
                else:
                    send_message(user_id,"Продолжайте",main_keyboard)
