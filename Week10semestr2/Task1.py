num1 = 1
net = []
while True:
    n = int(input())
    if n == 0:
        break

    s, t, c = map(int, input().split())
    
    cap = [[0] * (n + 1) for _ in range(n + 1)]
    for _ in range(c):
        u, v, w = map(int, input().split())
        cap[u][v] += w
        cap[v][u] += w
    
    def bfs(s, t, parent, cap):
        vis = [False] * (n + 1)
        queue = [s]
        vis[s] = True
        
        while queue:
            u = queue.pop(0)
            
            for v in range(1, n + 1):
                if not vis[v] and cap[u][v] > 0:
                    queue.append(v)
                    vis[v] = True
                    parent[v] = u
                    
        return vis[t]

    max1 = 0
    parent = [0] * (n + 1)
    
    while bfs(s, t, parent, cap):
        p_f = float('inf')
        v = t
        while v != s:
            u = parent[v]
            p_f = min(p_f, cap[u][v])
            v = u
            
        v = t
        while v != s:
            u = parent[v]
            cap[u][v] -= p_f
            cap[v][u] -= p_f
            v = u
            
        max1 += p_f
    
    net.append(max1)

for i, f in enumerate(net):
    print(f"Network {i+1}")
    print(f"The bandwidth is {f}.")
