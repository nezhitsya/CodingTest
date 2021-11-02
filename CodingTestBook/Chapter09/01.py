import sys

input = sys.stdin.readline
INF = int(1e9) # 10억 > 무한을 의미하는 값

n, m = map(int, input().split()) # 노드 개수, 간선 수
start = int(input()) # 시작노드
graph = [[] for i in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1) # 최단거리 테이블 초기화

for _ in range(m) :
    a, b, c = map(int, input().split()) # 간선 정보
    graph[a].append((b, c)) # a 노드에서 b 노드로 가는 비용 c

# 방문하지 않은 노드 중, 최단거리가 짧은 노드 번호 반환
def get_smallest_node() :
    min_value = INF
    index = 0 # 최단거리 노드 인덱스
    for i in range(1, n + 1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return index

# 다익스트라 알고리즘
def dijkstra(start) :
    distance[start] = 0
    visited[start] = True
    for j in graph[start] :
        distance[j[0]] = j[1]
    # 시작노드 제외 전체 n - 1 노드 반복
    for i in range(n - 1) :
        # 최단거리 노드 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 연결된 다른 노드 확인
        for j in graph[now] :
            cost = distance[now] + j[1]
            # 다른 노드 이동 거리가 더 짧은 경우
            if cost < distance[j[0]] :
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기위한 최단 거리 출력
for i in range(1, n + 1) :
    if distance[i] == INF : # 도달할 수 없는 경우
        print("INFINITY")
    else :
        print(distance[i])