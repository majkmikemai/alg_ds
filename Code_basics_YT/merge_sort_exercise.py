def merge_sort(arr, key="age", descending=True):
    if len(arr) <= 1:
        return

    if len(arr) > 1:
        mid = len(arr) // 2

        left_arr = arr[:mid]
        right_arr = arr[mid:]

        merge_sort(left_arr, key, descending)
        merge_sort(right_arr, key, descending)

    left_idx, right_idx, k_index = 0, 0, 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if (
            left_arr[left_idx][key] <= right_arr[right_idx][key]
            and not descending
            or (left_arr[left_idx][key] >= right_arr[right_idx][key] and descending)
        ):
            arr[k_index] = left_arr[left_idx]
            left_idx += 1

        else:
            arr[k_index] = right_arr[right_idx]
            right_idx += 1

        k_index += 1

    while left_idx < len(left_arr):
        arr[k_index] = left_arr[left_idx]
        left_idx += 1
        k_index += 1

    while right_idx < len(right_arr):
        arr[k_index] = right_arr[right_idx]
        right_idx += 1
        k_index += 1


if __name__ == "__main__":
    elements = [
        {"name": "vedanth", "age": 17, "time_hours": 1},
        {"name": "rajab", "age": 12, "time_hours": 3},
        {"name": "vignesh", "age": 21, "time_hours": 2.5},
        {"name": "chinmay", "age": 24, "time_hours": 1.5},
        {"name": "chinmay2", "age": 100, "time_hours": 1.5},
    ]
    merge_sort(elements, key="age", descending=True)
    print(elements)
