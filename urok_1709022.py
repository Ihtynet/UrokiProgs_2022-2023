
####################################
# УРОК - 17 сентября 2022
# ----------------------------------
# ЭМУЛЯТОР ИГРЫ "ОДНОРУКИЙ БАНДИТ"
# ----------------------------------
# Если выпадает три одинаковых слова, то выйгрыш - 100 000 руб
# Если выпадает два одинаковых слова, то выйгрыш - 100 руб
#
####################################
import random

mas = ["Яблоко","Груша","Банан","Арбуз","Авокадо","Малина","Дыня"]

r1 = random.randint(0, 6)
p1 = mas[r1]
r2 = random.randint(0, 6)
p2 = mas[r2]
r3 = random.randint(0, 6)
p3 = mas[r3]
print(p1, p2, p3)
if p1==p2 and p1==p3:
    print("Вы выйграли 100 000 рублей")
elif p1==p2 or p1==p3 or p1==p2:
    print("Вы выйграли 100 рублей")
