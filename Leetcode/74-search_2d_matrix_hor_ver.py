def searchMatrix(matrix, target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    bot, top = 0, rows - 1

    while bot <= top:
        mid_col = (bot + top) // 2
        if matrix[mid_col][-1] < target:
            bot = mid_col + 1
        elif matrix[mid_col][0] > target:
            top = mid_col - 1
        else:
            break
    if not (bot <= top):
        return False

    left, right = 0, cols - 1
    while left <= right:
        mid_row = (left + right) // 2
        if matrix[mid_col][mid_row] < target:
            right = mid_row - 1
        elif matrix[mid_col][mid_row] > target:
            left = mid_row + 1
        else:
            return True


if __name__ == "__main__":
    matrix = [[1, 3]]
    print(searchMatrix(matrix, 3))
