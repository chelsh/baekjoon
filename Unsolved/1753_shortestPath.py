import sys

V, E = [int(n) for n in sys.stdin.readline().split()]
K = int(sys.stdin.readline())

L = []
for _ in range(E):
    L.append([int(n) for n in sys.stdin.readline().split()])

dis = ['INF' for _ in range(V+1)]
dis[K] = 0

adj = [[] for _ in range(V+1)]
for i in range(E):
    u, v = L[i][0], L[i][1]
    adj[u].append(v)

connected = [0 for _ in range(V+1)]
connected[K] = 1
searched = [0 for _ in range(V+1)]
searched[K] = 1

def checkConnection(u):
    ad = adj[u]
    stop = 1
    for v in ad:
        if connected[v] == 0:
            connected[v] = 1
            checkConnection(v)
            stop = 0
    if stop == 1:
        return
checkConnection(K)

def search(u):
    if searched != connected:
        for v in adj[u]:
            


        for i in range(E):
            if L[i][0] == u:
                s, e, c = L[i]
                if dis[e] == 'INF':
                    dis[e] = dis[s] + c
                dis[e] = min(dis[e], dis[s] + c)
                searched[e] = 1
        

search(K)

for i in range(1, V+1):
    print(dis[i])