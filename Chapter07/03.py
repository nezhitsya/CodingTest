def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target :
            return mid
        # 중간점 값이 찾을 값보다 큰 경우 왼쪽 확인
        elif array[mid] > target :
            end = mid - 1
        # 중간점 값이 찾을 값보다 작은 경우 오른쪽 확인
        else :
            start = mid + 1
    return None

n = int(input()) # 개수
array = list(map(int, input().split())) # 전체 원소
array.sort()

m = int(input()) # 찾을 원소 개수
x = list(map(int, input().split())) # 찾을 원소

for i in x :
    result = binary_search(array, i, 0, n - 1)
    if result != None :
        print("yes", end=' ')
    else :
        print("no", end=' ')