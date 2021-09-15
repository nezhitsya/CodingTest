import sys

n = int(sys.stdin.readline())
first = 1
second = 2
tmp = 0

for i in range(n - 1):
    tmp = first
    first = second
    second = (tmp + second) % 15746
    
print(first)