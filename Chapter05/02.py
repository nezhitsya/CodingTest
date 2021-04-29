from collections import deque

# 큐(Queue) 구현을 위해서는 deque 라이브러리 필요
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력 [3, 7, 1, 4]
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력 [4, 1, 7, 3]