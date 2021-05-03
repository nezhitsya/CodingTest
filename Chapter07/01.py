def sequential_search(n, target, array) :
    for i in range(n) :
        if array[i] == target :
            return i + 1

data = input().split() # 원소 개수, 찾을 문자열 입력
n = int(data[0]) # 원소 개수
target = data[1] # 찾을 문자열

array = input().split() # n만큼 문자열 입력
print(sequential_search(n, target, array))