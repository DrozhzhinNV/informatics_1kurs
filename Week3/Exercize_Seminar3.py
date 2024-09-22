#Задача 1

def fib():
    n = int(input())

    fib_first = [1, 1]
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(2, n):
            fib_first.append(fib_first[i-1] + fib_first[i-2])
    return fib_first[-1]
print(fib())

#Задача 2

def prime_factors():
    n = int(input())
    a = ''

    for i in range(2, n//2 + 1):
        if n % i == 0:
            a += str(i) + ' '
    a += str(n)
    return a
print(prime_factors())

#Задача 3

#Найдём наибольший общий делитель через рекурсию
ls = list(map(int, input().split()))
a = ls[0]
b = ls[1]
def NOK(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif b > a:
        b = b % a
        print(a, b)
        return NOK(a, b)
    elif a > b:
        a = a % b
        return NOK(a, b)
print(NOK(a, b))
 #Смог только найти НОД, дальше не продвинулся

 #Задача 4

a = input().split()
size = int(a[0])
symb = a[1]

def triangle(size, symb):
    for i in range(size // 2 + size % 2):
        print(symb * (i + 1))
    for i in range(size // 2, 0, -1):
        print(symb * i)

triangle(size, symb)

#Задача 5

import numpy as np

#Функция, создающая спиральную матрицу M*N
def matrix():
    data = list(map(int, input('Введите кол-во строк и столбцов матрицы через пробел:').split()))
    m, n = data[0], data[1]
    a = np.zeros((m, n))
    a[0][0] = 1
    i = 0
    j = 1
    counter = 1

    while 0 in a:
        while j < n and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            j += 1
        j -= 1
        i += 1

        while i < m and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            i += 1
        i -= 1
        j -= 1

        while j > -1 and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            j -= 1
        j += 1
        i -= 1

        while i > -1 and a[i][j] == 0:
            a[i][j] = counter + 1
            counter += 1
            i -= 1
        i += 1
        j += 1
    return a

first_res = matrix()

#Функция, умножающая каждый элемент на номер строки, в которой он находится
def multiplication(first_res):
    for i in range(len(first_res)):
        first_res[i] = np.array(first_res[i]) * (i + 1)
    return first_res
print(multiplication(first_res))

#Задача 6

#В условии подразумевается, что мы считаем коэф. МНК для прямой линии (Уравнение y = ax + b)
#Если это было бы не так, в условии про наверное написали бы (Может я ошибаюсь)

import numpy as np

def mnk():
    mas_x = list(map(float, input('Введите набор измерений x:').split()))
    mas_y = list(map(float, input('Введите набор измерений y:').split()))

    if len(mas_x) != len(mas_y):
        print("Число измерений x должно быть равно числу измерений y")

    # См. Лабораторный практикум по общей физике. Том 1. Механика. Стр. 39
    b = (np.mean(np.array(mas_x) * np.array(mas_y)) - np.mean(mas_x) * np.mean(mas_y)) / (np.mean(np.array(mas_x) ** 2) - (np.mean(mas_x)) ** 2)
    a = np.mean(mas_y) - b * np.mean(mas_x)


    return float(a), float(b)

print(mnk())
#В ответе появляется очень много ненужных знаков после запятой из-за использования типа float, как это пофиксить я пока не очень понимаю

#Задача 7

import numpy as np
n = int(input('Кол-во строк:'))
m = int(input('Кол-во столбцов'))
#Параметр m здесь не нужен, но во входных данных он есть, поэтому PEP8 ругается

coeff = []
values = []
def linal(n ,m):
    for i in range(n):
        coeff.append(list(map(int, input().split())))
    if np.linalg.det(coeff) == 0:
        return 'Решений нет'
    else:
        for i in range(len(coeff)):
            values.append(coeff[i][-1])
            coeff[i] = coeff[i][:-1]
        return np.linalg.solve(coeff, values)

print(linal(n,m))
