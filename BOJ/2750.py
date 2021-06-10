n = int(input())
nums = list()

for i in range(n) :
    nums.append(int(input()))

nums.sort()

for i in nums :
    print(i)