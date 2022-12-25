# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input("Введите степень k - "))
mng = ""
data = open("mnogochlen.txt", 'w')
while k >= 0:
    rnd = random.randint(0, 10)
    if k != 0:
        if rnd !=0:
            mng += f"{str(rnd)}*x^{k} + "
    else:
        if rnd !=0:
            mng += f"{str(rnd)} = 0"
    k-=1
data.write(mng)
data.close()