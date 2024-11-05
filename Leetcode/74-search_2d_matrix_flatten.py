def searchMatrix(matrix, target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    nr_elements = rows * cols

    left = 0
    right = nr_elements - 1

    while left < right:
        mid = (left + right) // 2
        r = mid // cols
        c = mid % cols

        if matrix[r][c] < target:
            right = mid - 1
        elif matrix[r][c] > target:
            left = mid + 1
        else:
            return True
    return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(searchMatrix(matrix, 3))
