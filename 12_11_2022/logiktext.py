import datetime
import random
qw = True
while qw == True:
    t = input("Введите строку: ").lower()
    if t == "привет":
        print("Здравствуй, дорогой!")
    elif t == "как дела?":
        print("Пока все хорошо!")
    elif t=="сколько времени?":
        print("Сейчас: ", datetime.datetime.now().time())
    elif t == "какая погода?":
        pt = random.randint(-20,10)
        print("Температура: ", pt)
        if pt<-10:
            print("Сильно холодно")
        else:
            print("Немного холодновато")
    elif t=="выход":
        print("До свидания")
        qw = False
    else:
        print("Я не понял вопроса")