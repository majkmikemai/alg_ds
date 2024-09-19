# matrix = [[1, 2, 3, 1], [4, 5, 6, 1], [7, 8, 9, 1], [7, 8, 9, 1], [7, 8, 9, 1]]
matrix = [[-4, -5]]

prefix_sums = []

for rows in matrix:
    counter = 0
    row_sums = []
    for element in rows:
        counter += element
        row_sums.append(counter)
    prefix_sums.append(row_sums)


def range_sum_2d(row1, col1, row2, col2):
    # Ensure start_row and end_row are valid (within matrix range)
    if row1 < 0 or row2 >= len(matrix) or row1 > row2:
        print("Invalid row range")
        return

    # Loop through each row between start_row and end_row (inclusive)
    total_sum = 0
    for i in range(row1, row2 + 1):
        right = prefix_sums[i][col2]
        left = prefix_sums[i][col1 - 1] if col1 > 0 else 0
        total_sum += right - left

    return total_sum


print(prefix_sums)
print(range_sum_2d(0, 0, 0, 1))
