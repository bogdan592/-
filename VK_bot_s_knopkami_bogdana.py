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
fortunka_keyboard.add_line()
fortunka_keyboard.add_button('Баланс')

back_keyboard = VkKeyboard(one_time = True)
back_keyboard.add_button('Назад')

number_keyboard = VkKeyboard(one_time = True)
number_keyboard.add_button('Тяжёлая сложность')
number_keyboard.add_line()
number_keyboard.add_button('Средняя сложность')
number_keyboard.add_line()
number_keyboard.add_button('Лёгкая сложность')
number_keyboard.add_line()
number_keyboard.add_button('Назад')
gamer={}
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
                      send_message(user_id,"Проигрышь,жизни кончились ಥ_ಥ,правильный ответ:"+str(gamers[user_id]['goal']))
                      del gamers[user_id]
                                    
                if otvet > goal:                      
                    send_message(user_id,"❌Много❌,осталось жизней "+str(gamers[user_id]['lives']))
                    gamers[user_id]['lives'] -= 1
                elif otvet < goal:
                    send_message(user_id,"❌Мало❌,осталось жизней "+str(gamers[user_id]['lives']))
                    gamers[user_id]['lives'] -= 1
                else:
                    send_message(user_id,"✅Победа!!!✅ 🥳", main_keyboard)
                    del gamers[user_id]
                
                def fortun (user_id,play,balance,number):                                                                                   
                    play = gamer[user_id]['play']                         
                    balance = gamer[user_id]['balance']  
                    number = gamer[user_id]['number']  

                    if play < number:                      
                           send_message(user_id,"❌К сожалению ты проиграл❌.Твой баланс был обнулён",fortunka_keyboard)
                           gamers[user_id]['balance'] = 0
                    elif play > number:
                           send_message(user_id,"❌К сожалению ты проиграл❌.Твой баланс был обнулён",fortunka_keyboard)
                           gamers[user_id]['balance'] = 0
                    else:
                        send_message(user_id,"✅Поздравляю вы выйграли✅!!!.На ваш баланс было зачисленно 500 рублей",fortunka_keyboard)
                    fortunka_keyboard
                    gamer[user_id]['balance'] += 500                                                 
                    del gamer[user_id]
            else:                    
                if text == 'START'.lower():   
                      send_message(user_id,"Добро пожаловать",main_keyboard)  # <===
                elif text == 'Об авторе'.lower():   
                       send_message(user_id,"Bogdan",back_keyboard)
                elif text == 'Сделать пожертвование'.lower():   
                       send_message(user_id,'Если хочешь можешь отправить мне денги по этой ссылке:https://www.donationalerts.com/r/bogdan1234567434',back_keyboard)
                elif text == 'Тяжёлая сложность'.lower():
                    from random import randint
                    gamers[user_id] = {'goal' : randint(1,8196),
                                       'lives': 15}
                    send_message(user_id,"Угадывай число от 1 до 8196 🤔.У тебя 15 попыток!😏")
                elif text == 'Средняя сложность'.lower():
                   from random import randint
                   gamers[user_id] = {'goal' : randint(1,4000),
                                       'lives': 10}
                   send_message(user_id,"Угадывай число от 1 до 4000 🤔. У тебя 10 попыток!😏")
                elif text == 'Лёгкая сложность'.lower():
                   from random import randint
                   gamers[user_id] = {'goal' : randint(1,200),
                                       'lives': 8}
                   send_message(user_id,'Угадывай число от 1 до 200 🤔. У тебя 8 попыток!😏')
                   
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
                elif text == 'Баланс'.lower():                    
                    send_message(user_id,"Ваш баланс:",fortun_keyboard)
                elif text == 'Поиграться'.lower():                    
                    send_message(user_id,"Выбирай игру",gamer_keyboard)
                elif text == 'Угадай число'.lower():                    
                    send_message(user_id,"Выбирай сложность",number_keyboard)
                elif text == 'Фортуна'.lower():                    
                    send_message(user_id,"Бланодаря этой игре ты можешь разбогатеть",fortun_keyboard)              
                elif text == 'Правила'.lower():                    
                    send_message(user_id,"В этой игре есть единственная кнопка:Разбогатеть.Шанс выйграть 50/50.Если ты проиграешь то все заработанные деньги сгорят,так что не увлекайся!Удачи!!!",fortun_keyboard)
                elif text == 'Начать игру'.lower():                    
                    send_message(user_id,"Все деньги в твоих руках!",fortunka_keyboard)
                elif text == 'Испытать удачу!'.lower():                                          
                     send_message(user_id,"Произошла неожиданная ошибка.Нажмите на любую кнопку чтобы продолжить")       
                     from random import randint
                     {'number' : 2,
                      'play': randint(1,3),
                      'balance': 0}
                                                         
                else:
                    send_message(user_id,"Продолжайте",main_keyboard)

