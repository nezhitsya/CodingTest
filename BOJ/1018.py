n, m = map(int, input().split())
board = [input() for _ in range(n)]

def count(x, y, z) :
    cnt = 0
    for i in range(8) :
        for j in range(8) :
            if i % 2 == 0 :
                if j % 2 == 0:
                    if board[i + x][j + y] == z[0] :
                        continue
                    cnt += 1
                else :
                    if board[i + x][j + y] == z[1] :
                        continue
                    cnt += 1
            else :
                if j % 2 == 0 :
                    if board[i + x][j + y] == z[1] :
                        continue
                    cnt += 1
                else :
                    if board[i + x][j + y] == z[0] :
                        continue
                    cnt += 1
    return cnt

result = []
for i in range(n - 7) :
    for j in range(m - 7) :
        result.append(count(i, j, ['W', 'B']))
        result.append(count(i, j, ['B', 'W']))

print(min(result))