import sys
import heapq

V, E = [int(n) for n in sys.stdin.readline().split()]
K = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]

INF = 10 ** 8

distance = [INF] * (V+1)

for _ in range(E):
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u].append((v, w))

def dijkstra(start):
    distance[start] = 0
    heap = [(0, start)]

    while len(heap) > 0:
        d, u = heapq.heappop(heap)

        if d > distance[u]:
            continue

        for v, w in graph[u]:
            new_dist = d + w
            if new_dist < distance[v]:
                distance[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

dijkstra(K)

result = []
for i in range(1, V+1):
    result.append('INF' if distance[i] == INF else str(distance[i]))
sys.stdout.write('\n'.join(result))