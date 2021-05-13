from collections import deque
import copy

v = int(input()) # 노드의 개수
indegree = [0] * (v + 1) # 모든 노드의 진입차수 0 초기화
graph = [[] for i in range(v + 1)] # 간선 정보 리스트 초기화
time = [0] * (v + 1) # 시간 0으로 초기화

for i in range(1, v + 1) :
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1] :
        indegree[i] += 1
        graph[x].append(i)

# 위상 정렬 함수
def topology_sort() :
    result = copy.deepcopy(time) # 알고리즘 수행 결과 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리

    # 진입 차수가 0인 노드 큐에 삽입
    for i in range(1, v + 1) :
        if indegree[i] == 0 :
            q.append(i)

    # 큐가 빌때까지 반복
    while q :
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수 -1
        for i in graph[now] :
            result[i] = max(result[i], result[now] + time[i])
            indegree -= 1
            # 새롭게 진입차수 0이되는 노드 큐에 삽입
            if indegree[i] == 0 :
                q.append(i)

    for i in range(1, v + 1) :
        print(result[i])

topology_sort()