# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
user_num = float(input("Введите вещественное число - "))
d = 0.1
degree = 1
while d > 10 ** (-10):
    print("{:.{k}f}".format(user_num, k = degree) + " при точности равной d = " + "{:.{k}f}".format(d, k = degree))
    d *= 0.1
    degree += 1
