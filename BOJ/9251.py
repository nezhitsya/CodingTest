import sys
input = lambda : sys.stdin.readline().strip()

a = input()
b = input()
l = [[0] * (len(b) + 1) for i in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            l[i][j] = l[i - 1][j - 1] + 1
        else:
            l[i][j] = max(l[i][j - 1], l[i - 1][j])

print(l[-1][-1])