"""
Largest product in a grid
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?
"""
grid = [[int(i) for i in input().split()]]
for i in range(len(grid[0]) - 1):
    add_row = [int(i) for i in input().split()]
    grid.append(add_row)
max_hor = 0
max_ver = 0
max_dia = 0
max_negativ_dia = 0
for i in range(len(grid) - 3):
    for j in range(len(grid)):
        pret_max_ver = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
        if max_ver < pret_max_ver:
            max_ver = pret_max_ver
        if j > 2:
            pret_max_negativ_dia = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]
            if max_negativ_dia < pret_max_negativ_dia:
                max_negativ_dia = pret_max_negativ_dia
        if j < 7:
            pret_max_dia = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
            if max_dia < pret_max_dia:
                max_dia = pret_max_dia
            pret_max_hor = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
            if pret_max_hor > max_hor:
                max_hor = pret_max_hor
print(max(max_hor, max_ver, max_dia, max_negativ_dia))