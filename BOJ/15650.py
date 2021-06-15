n, m = map(int, input().split())

arr = []
def f(start) :
    if len(arr) == m :
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, n + 1) :
        if i in arr :
            continue
        arr.append(i)
        f(i + 1)
        arr.pop()

f(1)