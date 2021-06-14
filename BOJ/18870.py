import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr1 = list(sorted(set(arr)))
dic = {value: index for index, value in enumerate(arr1)}

for i in arr :
    print(dic[i], end=" ")