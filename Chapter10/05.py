from collections import deque

v, e = map(int, input().split()) # 노드, 간선 개수
indegree = [0] * (v + 1) # 모든 노드 진입차수 0
graph = [[] for i in range(v + 1)] # 연결 리스트 (그래프)

# 방향 그래프의 모든 간선 정보 입력
for _ in range(e) :
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 a에서 b로 이동
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort() :
    result = [] # 알고리즘 수행 결과 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리

    # 진입 차수가 0인 노드 큐에 삽입
    for i in range(1, v + 1) :
        if indegree[i] == 0 :
            q.append(i)

# 큐가 빌때까지 반복
    while q :
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수 -1
        for i in graph[now] :
            indegree[i] -= 1
            # 새롭게 진입차수 0이되는 노드 큐에 삽입
            if indegree[i] == 0 :
                q.append(i)

    for i in result :
        print(i, end = ' ')

topology_sort()