array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array) :
    # 원소 개수 1 이하인 경우
    if len(array) <= 1 :
        return array
    pivot = array[0]
    tail = array[1:] # 피벗 제외 리스트

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽 오른쪽 부분 각각 정렬 수행 후 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))