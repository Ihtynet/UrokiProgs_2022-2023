# создаем переменную f и считываем в нее файл
f = open("input.txt", encoding="utf=8")

# создаем переменную mas и помещаем в нее массив строк
# mas = f.readlines() - это со знаком переноса строки
# или так
# mas = f.read().split("\n") - это без знака переноса строки

mas = f.read().split("\n")

# Выводим на экран содержимое массива
print(mas)

# Подсчитываем содержимое массива
dl = len(mas)

# Получаем элементы массива
print(mas[0]+mas[3])
