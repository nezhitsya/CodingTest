n, w = 4, 5
bag = [(2, 3), (3, 4), (4, 5), (5, 6)]
knap = [0 for _ in range(w + 1)]

for i in range(n):
    for j in range(w, 1, -1):
        if bag[i][0] <= j:
            knap[j] = max(knap[j], knap[j - bag[i][0]] + bag[i][1])

print(knap)