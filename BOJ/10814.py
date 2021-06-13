import sys

n = int(sys.stdin.readline())
user = []

for _ in range(n) :
    user.append(list(input().split()))

user.sort(key=lambda a:int(a[0]))

for i in range(n) :
    print(user[i][0], user[i][1])