import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def horizontal(x, val) :
    if val in sudoku[x] :
        return False
    return True

def vertical(y, val) :
    for i in range(9) :
        if val == sudoku[i][y] :
            return False
    return True

def square(x, y, val) :
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3) :
        for j in range(3) :
            if val == sudoku[nx + i][ny + j] :
                return False
    return True

def DFS(index) :
    if index == len(zero) :
        for row in sudoku :
            for n in row :
                print(n, end=" ")
            print()
        sys.exit(0)
    else :
        for i in range(1, 10) :
            nx = zero[index][0]
            ny = zero[index][1]

            if horizontal(nx, i) and vertical(ny, i) and square(nx, ny, i) :
                sudoku[nx][ny] = i
                DFS(index + 1)
                sudoku[nx][ny] = 0

DFS(0)