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

n, m = map(int, input().split()) # 노드, 간선 개수
parent = [0] * (n + 1) # 부모 테이블 초기화

for i in range(1, n + 1) :
    parent[i] = i # 부모를 자기 자신으로 초기화

for i in range(m) :
    oper, a, b = map(int, input().split())
    # 합잡합 연산인 경우
    if oper == 0 :
        union_parent(parent, a, b)
    # 찾기 연산인 경우
    elif oper == 1 :
        if find_parent(parent, a) == find_parent(parent, b) :
            print('YES')
        else :
            print("NO")