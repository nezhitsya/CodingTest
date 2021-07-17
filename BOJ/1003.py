t = int(input())

def fibonacci(i) :
    if i == 0 :
        print(1, 0)
    elif i == 1 :
        print(0, 1)
    elif i == 2 :
        print(1, 1)
    else :
        temp = 0
        current = 1
        before = 0
        for j in range(i - 1) :
            temp = current
            current = before + temp
            before = temp
        print(before, current)

for _ in range(t) :
    n = int(input())
    fibonacci(n)