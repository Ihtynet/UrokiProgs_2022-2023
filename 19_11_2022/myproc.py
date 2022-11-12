import datetime
import random

def get_otvet(stroka):

    if "привет" in stroka:
        otvet = "Здравствуй, дорогой!"
    elif "как дела" in stroka:
        otvet = "Пока все хорошо!"
    elif stroka == "выход" or  stroka == "конец" or  stroka == "q":
        otvet = "До свидания"
    else:
        otvet = "Я не понял вопроса"

    return otvet