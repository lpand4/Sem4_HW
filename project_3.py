#Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
user_str = (input("Введите последовательность - ").split())
for i in user_str:
    if user_str.count(i) == 1:
        print(i, end = " ")