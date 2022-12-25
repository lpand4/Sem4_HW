#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
user_num = int(input("Введите число - "))
i=2
while user_num > 0:
    if user_num%i == 0:
        print(i, end=' ')
        user_num//=i
    else:
        i+=1