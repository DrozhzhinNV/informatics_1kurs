a1 = open('INPUT.txt', 'r')
a2 = open('OUTPUT.txt', 'w')

mas = []
for line in a1:
    mas.append(list(map(int, line.split()))) 

N = mas[0][0]
G = mas[1:]

visited = [0 for _ in range(N)]
c = 0

for i in G:

    if visited[i[0] - 1] == 0:
        visited[i[0] - 1] = 1

    if visited[i[1] - 1] == 0:
        if visited[i[0] - 1] == 1:
            visited[i[1] - 1] = 2
        else:
            visited[i[1] - 1] = 1

    if visited[i[1] - 1] == visited[i[0] - 1]:
        a2.write('NO')
        c = 1
        break

if c == 0:
    a2.write('YES')