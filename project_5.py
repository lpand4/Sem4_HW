# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
import random


# Задает два рандомных многочлена
def rndmnogochlen(name):
    data = open(name, 'w')
    mng = ''
    k1 = random.randint(1, 4)
    while k1 >= 0:
        rnd = random.randint(0, 9)
        if k1 != 0:
            if rnd != 0:
                mng += f"{str(rnd)}*x^{k1} + "
        else:
            if rnd != 0:
                mng += f"{str(rnd)} "
            else:
                mng += "0 "
        k1 -= 1
    mng += "= 0"
    data.write(mng)
    data.close()
#Считает и возвращает кортеж из степени и коэфициента
def sum(mng1, mng2):
    res1 = {} #Первый многочлен его коэфициенты
    res2 = {} #Второй многочлен его коэфициенты
    res3 = {} #Сумма многочленов его коэфициенты
    for i in range(len(mng1)-1):
        res1[mng1[i][-1]] = mng1[i][0]
    res1[0] = int(mng1[len(mng1)-1])
    for i in range(len(mng2)-1):
        res2[mng2[i][-1]] = mng2[i][0]
    res2[0] = int(mng2[len(mng2)-1])
    for keys in res1:
        if keys in res2:
            res3[int(keys)] = int(res1[keys])+int(res2[keys])
        elif keys not in res2:
            res3[int(keys)] = int(res1[keys])
    for keys in res2:
        if keys not in res1:
            res3[int(keys)] = int(res2[keys])
    return res3




#Задаем и записываем в файлы рандомные многочлены
rndmnogochlen("mnogochlen1.txt")
rndmnogochlen("mnogochlen2.txt")
# Считываем с файлов эти многочлены
mnogochlen1 = open('mnogochlen1.txt', 'r')
mnogochlen2 = open('mnogochlen2.txt', 'r')
mng1 = mnogochlen1.read().split()
mng2 = mnogochlen2.read().split()
# Удаляем лишнее, оставляем только одночлены
for i in mng1:
    if i == "+" or i == "=":
        mng1.remove(i)
del mng1[len(mng1) - 1]
for i in mng2:
    if i == "+" or i == "=":
        mng2.remove(i)
del mng2[len(mng2) - 1]
print(mng1)
print(mng2)
mnogochlen1.close()
mnogochlen2.close()
#Запускаем функцию суммы и сортируем
result = sorted(sum(mng1, mng2).items(),reverse=1)
msg =""
# Записываем результативный многочлен
for i in result:
    if i[0] != 0:
        msg +=f'{i[1]}*x^{i[0]} + '
    else:
        msg +=f'{i[1]} = 0 '
mng_sum = open("summ_of_mnogochlen.txt", 'w')
print(msg)
mng_sum.write(msg)
mng_sum.close()