n, m = map(int, input().split()) # n X m

# 2차원 리스트 맵 정보
graph = []
for i in range(n) :
    graph.append(list(map(int, input())))

def dfs(x, y) :
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False
    # 0인 경우
    if graph[x][y] == 0 :
        # 해당 노드 1로 변경
        graph[x][y] = 1
        # 상, 하, 좌, 우 위치 재귀적 호출 > 0인 경우 1로 변경
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            result += 1

print(result)
