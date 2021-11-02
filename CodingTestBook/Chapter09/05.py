import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 10억 > 무한을 의미하는 값

n, m, start = map(int, input().split()) # 노드 개수, 간선 수, 시작 노드
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1) # 최단 거리 테이블 무한으로 초기화

for _ in range(m) :
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 큐가 비어있지 않는 동안
    while q :
        # 최단 거리가 짧은 노드 정보
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        # 연결된 다르 인접 노드 확인
        for i in graph[now] :
            cost = dist + i[1]
            # 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

count = 0 # 도달할 수 있는 노드 수
max_distance = 0 # 도달할 수 있는 노드 중 가장 멀리 있는 노드의 최단 거리
for d in distance :
    if d != INF :
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance)