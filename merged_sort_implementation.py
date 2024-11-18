# def merge_sort(arr):
#     if len(arr) <= 1:
#         return

#     mid = len(arr) // 2
#     left = arr[:mid]
#     right = arr[mid:]

#     merge_sort(left)
#     merge_sort(right)

#     merged_two_list(left, right, arr)


# def merged_two_list(a, b, arr):
#     left = len(a)
#     right = len(b)

#     i, j, k = 0, 0, 0
#     while i < left and j < right:
#         if a[i] <= b[j]:
#             arr[k] = a[i]
#             i += 1

#         else:
#             arr[k] = b[j]
#             j += 1
#         k += 1

#     while i < left:
#         arr[k] = a[i]
#         i += 1
#         k += 1

#     while j < right:
#         arr[k] = b[j]
#         j += 1
#         k += 1


def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_list(left, right, arr)


def merge_two_list(left, right, arr):
    l = len(left)
    r = len(right)

    i, j, k = 0, 0, 0

    while i < l and j < r:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < l:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < r:
        arr[k] = right[j]
        j += 1
        k += 1


if __name__ == "__main__":
    a = [2, 81, 41, 52, 30]
    merge_sort(a)
    print(a)

# import numpy as np

# # Example 2D array (matrix)
# matrix = np.array([[1, 2, 3], [4, 5, 6]])

# # Flattening the matrix
# flattened_matrix = matrix.flatten()

# print(flattened_matrix)
