data = input() # 행(문자) + 열(숫자)
row = int(data[1])

# ord() : 문자의 유니코드 값 반환
# 입력받은 문자 ASCII - a의 ASCII + 1
column = int(ord(data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

count = 0

for step in steps :
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
        count += 1
    
print(count)