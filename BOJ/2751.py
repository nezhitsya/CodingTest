import sys

n = int(sys.stdin.readline())
nums = list()
result = list()

for i in range(n) :
    nums.append(int(sys.stdin.readline()))

result = sorted(nums)

for i in result :
    print(i)