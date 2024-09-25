def merge_sort(arr):
    if len(arr) <= 1:
        return

    if len(arr) > 1:
        mid = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr)
        merge_sort(right_arr)

    left_idx, right_idx, k_index = 0, 0, 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            arr[k_index] = left_arr[left_idx]
            left_idx += 1
        else:
            arr[k_index] = right_arr[right_idx]
            right_idx += 1
        k_index += 1
    if left_idx < len(left_arr):
        arr[k_index] = left_arr[left_idx]
        left_idx += 1
        k_index += 1

    if right_idx < len(right_arr):
        arr[k_index] = right_arr[right_idx]
        right_idx += 1
        k_index += 1


if __name__ == "__main__":
    arr = [5, 3, 4, 2]
    merge_sort(arr)
    print(arr)
