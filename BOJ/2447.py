n = int(input())
star = [[' ' for _ in range(n)] for _ in range(n)]

def fill_square(size, x, y) :
    if size == 1 :
        star[y][x] = "*"
    else :
        next_size = size // 3
        for dy in range(3) :
            for dx in range(3) :
                if dy != 1 or dx != 1 :
                    fill_square(next_size, x + dx * next_size, y + dy * next_size)

fill_square(n, 0, 0)
for k in star :
    print(''.join(k))