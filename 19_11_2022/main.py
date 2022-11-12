
import myproc as mp

qw = True
while qw == True:
    t = input("Введите строку: ").lower()
    ot = mp.get_otvet(t)
    print(ot)

    if ot == "До свидания":
        qw = False
