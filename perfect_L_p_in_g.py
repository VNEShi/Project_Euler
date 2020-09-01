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
largest = 0
for i in range(len(grid) - 3):
    for j in range(len(grid) - 3):
        pred_largest = max((grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]),
                            (grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]),
                            (grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]),
                            (grid[i + 3][j] * grid[i + 2][j + 1] * grid[i + 1][j + 2] * grid[i][j + 3]))
        largest = max(largest, pred_largest)
print(largest)