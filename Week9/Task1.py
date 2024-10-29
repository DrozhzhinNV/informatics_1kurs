a = input()
priority = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
}

#Разобьём на список
a1 = []
k = ''
for i in a:
    if i != '+' and i != '-' and i != '*' and i != '/' and i != '(' and i != ')':
        k += i
    elif k != '':
        a1.append(k)
        a1.append(i)
        k = ''
    else:
        a1.append(i)
if k != '':
    a1.append(k)

#Расставим приоритеты
k = 0
pr = []
for i in a1:
    if i == '(':
        k += 10
    elif i == ')':
        k -= 10
    elif i in priority:
        pr.append(priority[i] + k)
    else:
        pr.append(0)
pr1 = pr

#Удалим из нашего списка элементов скобочки
for i in a1:
    if i == '(' or i == ')':
        a1.remove(i)


res1 = []

while max(pr) != -1:
    for i in range(len(pr)):
        if pr[i] == max(pr) and pr[i+1] == 0 and pr[i-1] == 0:
            res1.append(a1[i-1])
            res1.append(a1[i+1])
            res1.append(a1[i])
            pr[i] = -1
            pr[i-1] = -1
            pr[i+1] = -1
            break
        if pr[i] == max(pr) and pr[i+1] == -1 and pr[i-1] == -1:
            res1.append(a1[i])
            pr[i] = -1
            break
print(' '.join(res1))
