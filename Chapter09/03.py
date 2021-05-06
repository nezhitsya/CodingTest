INF = int(1e9) # 10억 > 무한을 의미하는 값

n, m = map(int, input().split()) # 노드 개수, 간선 수
graph = [[INF] * (n + 1) for _ in range(n + 1)] # 2 차원 리스트 모든 값 무한

# 자기 자신으로 가는 비용 0
for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if a == b :
            graph[a][b] = 0

# 간선 정보 입력
for _ in range(m) :
    # a 에서 b로 가는 비용 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n + 1) :
    for a in range(1, n + 1) :
        for b in range(1, n + 1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1) :
    for b in range(1, n + 1) :
        if graph[a][b] == INF :
            print("INFINITY")
        else :
            print(graph[a][b], end = " ")
    print()