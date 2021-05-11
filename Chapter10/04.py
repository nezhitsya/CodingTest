def find_parent(parent, x) :
    # 루트 노드가 아닌 경우, 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 union
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b

v, e = map(int, input().split()) # 노드, 간선 개수
parent = [0] * (v + 1) # 부모 테이블 초기화

edges = [] # 모든 간선 리스트
result = 0 # 최종 비용

for i in range(1, v + 1) :
    parent[i] = i # 부모를 자기 자신으로 초기화

# 모든 간선에 대한 정보 입력
for _ in range(e) :
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 튜플 첫 번째 원소 비용으로 설정

edges.sort() # 간선 비용 순으로 정렬

for edge in edges :
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b) :
        union_parent(parent, a, b)
        result += cost

print(result)