n, m = map(int, input().split())

arr = []
def f(depth, n, m) :
    if depth == m :
        print(' '.join(map(str, arr)))
        return
    
    for i in range(n) :
        arr.append(i + 1)
        f(depth + 1, n, m)
        arr.pop()

f(0, n, m)