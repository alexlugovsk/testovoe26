def findIntByFibonachi(n):
    """
    возвращает ближайшее от переданного числа число из
    последовательности Фибоначчи
    :param n: переданное число
    :return: ближайшее число из последовательности
    """
    n = int(n) #преобразуем на всякий случай, если вдруг сюда число строкой передадут
    a=b=1
    while 2*n>a+b:a,b=b,a+b
    return a
