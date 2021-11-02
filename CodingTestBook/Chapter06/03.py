array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end) :
    # 원소 개수 1인 경우
    if start >= end :
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right :
        # 피벗보다 큰 데이터 발견까지
        while left <= end and array[left] <= array[pivot] :
            left += 1
        # 피벗보다 작은 데이터 발견까지
        while right > start and array[right] >= array[pivot] :
            right -= 1
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        else :
            array[left], array[pivot] = array[pivot], array[left]
    # 분할 이후 왼쪽 오른쪽 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
