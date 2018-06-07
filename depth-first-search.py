def dfs(matrix, row, column):
    if row < 0 or column < 0 or row >= len(matrix) or column >= len(matrix[row]):
        return 0

    if matrix[row][column] == 0:
        return 0

    matrix[row][column] = 0

    result = 1
    result += dfs(matrix, row + 1, column)
    result += dfs(matrix, row - 1, column)
    result += dfs(matrix, row, column + 1)
    result += dfs(matrix, row, column - 1)
    result += dfs(matrix, row + 1, column + 1)
    result += dfs(matrix, row - 1, column - 1)
    result += dfs(matrix, row - 1, column + 1)
    result += dfs(matrix, row + 1, column - 1)
    return result


def getBiggerRegion(grid):
    result = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 1:
                result = max(result, dfs(grid, row, column))
    return result


n = 4
m = 4
l = ['1 1 0 0', '0 1 1 0', '0 0 1 0', '1 0 0 0']
grid = []
for _ in l:
    grid.append(list(map(int, _.rstrip().split())))
print(getBiggerRegion(grid))
