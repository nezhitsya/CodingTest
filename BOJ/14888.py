n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_num, max_num = 1e9, -1e9

def dfs(i, res, add, sub, mul, div) :
    global max_num, min_num
    if i == n :
        max_num = max(res, max_num)
        min_num = min(res, min_num)
        return
    else :
        if add :
            dfs(i+1, res+nums[i], add-1, sub, mul, div)
        if sub :
            dfs(i+1, res-nums[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)

dfs(1, nums[0], add, sub, mul, div)
print(max_num)
print(min_num)