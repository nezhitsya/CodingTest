n, m = map(int, input().split())

arr = []
def f(depth, index, n, m) :
    if depth == m :
        print(' '.join(map(str, arr)))
        return
    
    for i in range(index, n) :
        arr.append(i + 1)
        f(depth + 1, i, n, m)
        arr.pop()

f(0, 0, n, m)