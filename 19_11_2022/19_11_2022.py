def scht(a,b):
    r=0
    if len(a)>len(b):
        r = len(a)
    else:
        r = len(b)
    return r

p1 = input("Введите слово 1")
p2 = input("Введите слово 2")
dl = scht(p1,p2)
print("Длина самого длинного слова: "+str(dl))