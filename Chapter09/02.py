import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 10억 > 무한을 의미하는 값

n, m = map(int, input().split()) # 노드 개수, 간선 수
start = int(input()) # 시작노드
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1) # 최단거리 테이블 초기화

for _ in range(m) :
    a, b, c = map(int, input().split()) # 간선 정보
    graph[a].append((b, c)) # a 노드에서 b 노드로 가는 비용 c

# 다익스트라 알고리즘
def dijkstra(start) :
    q =[]
    # 시작 노드로 가기 위한 최단 경로 0, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 빈 큐가 아닌 경우
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        # 연결된 다른 노드 확인
        for i in graph[now] :
            cost = dist + i[1]
            # 다른 노드 이동 거리가 더 짧은 경우
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)

# 모든 노드로 가기위한 최단 거리 출력
for i in range(1, n + 1) :
    if distance[i] == INF : # 도달할 수 없는 경우
        print("INFINITY")
    else :
        print(distance[i])