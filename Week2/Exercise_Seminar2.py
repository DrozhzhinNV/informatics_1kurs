#Задача 1

a = list(map(int, input().split()))
b = [i for i in range(1, len(a) + 1)]

for i in range(len(b)):
    if b[i] not in a[1:]:
        print(b[i])

#Задача 2

a = list(input().split())
print(a)
line_ls = [i for i in a[1]]
b = ''

for i in range(0, len(a[1]), int(a[0])):
    b += ''.join(reversed(line_ls[i:i + int(a[0])]))
print(b)

#Задача 4

a = list( input().split())
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join(a))  #Просто вывод. Основная задача решена в три строки

#Задача 5

a = input().split()
a = a[-1:] + a[:-1]

print(' '.join(a)) #Просто вывод. Основная задача решена в 2 строки

#Задача 6

a = input().split()
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a[i], end=' ')

#Задача 7

a = input().split()
b = 0
for i in range(len(a)):
    if a.count(a[i]) > b:
        b = int(a[i])
print(b)

#Задача 8

N = int(input()) #Не очень понятно, зачем вводится число N
bigger = 0
smaller = 0
a = list(map(int, input().split()))
for i in a:
    for g in range(len(a)):
        if a[g] < i:
            smaller += 1
        elif a[g] > i:
            bigger += 1
    if smaller == bigger:
        print(i)
        break


