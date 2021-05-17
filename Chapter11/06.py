# 프로그래머스 사이트 참조

import heapq

def solution(food_times, k) :
    if sum(food_times) <= k :
        return -1

    # 시간이 적은 것 부터 빼기 위해 우선순위 큐 사용
    q = []
    for i in range(len(food_times)) :
        # (시간, 번호) 형태로 큐에 삽입
        heapq.heappush(1, (food_times[i], i + 1))
    sum_value = 0 # 사용 시간
    previous = 0 # 직전 시간
    length = len(food_times) # 남은 개수

    # sum + (현재 시간 - 이전 시간) * 현재 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now # 이전 시간 재설정

    # 몇 번째인지 출력
    result = sorted(q, key = lambda x: x[1]) # 번호 기준 정렬
    return result[(k - sum_value) % length][1]