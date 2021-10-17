n = int(input())
stair = list()

for i in range(n):
    stair.append(int(input()))

score = list()
score.append(stair[0])
score.append(stair[0] + stair[1])
score.append(max(stair[2] + stair[0], stair[2] + stair[1]))

for i in range(3, n):
    score.append(max(stair[i] + score[i - 2], stair[i] + score[i - 1] + score[i - 3]))

print(score[0]) 