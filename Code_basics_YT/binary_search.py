import time


def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1


def binary_search(numbers_list, number_to_find):
    left_idx = 0
    right_idx = len(numbers_list) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2

        if numbers_list[mid_idx] < number_to_find:
            left_idx = mid_idx + 1

        elif numbers_list[mid_idx] > number_to_find:
            right_idx = mid_idx - 1
        else:
            return mid_idx
    return -1


def rec_binary_search(
    numbers_list, number_to_find, left_index, right_index, element_index=None
):
    if element_index is None:
        element_index = []

    if right_index < left_index:
        return element_index
    mid_idx = (left_index + right_index) // 2

    if numbers_list[mid_idx] == number_to_find:
        # Append if the value is found in the list
        element_index.append(mid_idx)
        # # Check left side if there exist more of the same value
        # rec_binary_search(
        #     numbers_list, number_to_find, left_index, mid_idx - 1, element_index
        # )
        # # Check right side if there exist more of the same value
        # rec_binary_search(
        #     numbers_list, number_to_find, mid_idx + 1, right_index, element_index
        # )

    # Go to the right side
    if numbers_list[mid_idx] < number_to_find:
        left_index = mid_idx + 1
        return rec_binary_search(
            numbers_list, number_to_find, left_index, right_index, element_index
        )

    # Go to the left side
    elif numbers_list[mid_idx] > number_to_find:
        right_index = mid_idx - 1
        return rec_binary_search(
            numbers_list, number_to_find, left_index, right_index, element_index
        )
    else:  # If value is found
        return sorted(element_index)


def find_all_occurances(numbers_list, number_to_find):
    element_index = binary_search(numbers_list, number_to_find)

    if element_index == -1:
        return []

    indices = [element_index]

    left_index = element_index - 1

    while left_index >= 0:
        if numbers_list[left_index] == number_to_find:
            indices.append(left_index)
            left_index -= 1
        else:
            break

    right_index = element_index + 1
    while right_index < len(numbers_list):
        if numbers_list[right_index] == number_to_find:
            indices.append(left_index)
            right_index += 1
        else:
            break
    return sorted(indices)


if __name__ == "__main__":
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find = 45

    # numbers_list = [i for i in range(1000001)]
    # number_to_find = 100000

    numbers_list = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    number_to_find = 15

    # start_time_ls = time.time()
    # ls_result = linear_search(numbers_list, number_to_find)
    # end_time_ls = time.time()

    # start_time_bs = time.time()
    # bs_result = binary_search(numbers_list, number_to_find)
    # end_time_bs = time.time()

    # elapsed_time_ls = end_time_ls - start_time_ls
    # elapsed_time_bs = end_time_bs - start_time_bs
    # print(f"Running Linear search, the value can be found at index {ls_result}")
    # print(f"The code ran for {elapsed_time_ls}")

    # print(f"Running Binary search, the value can be found at index {bs_result}")
    # print(f"The code ran for {elapsed_time_bs} s")

    # rbs = rec_binary_search(numbers_list, number_to_find, 0, len(numbers_list))
    # print(rbs)
    find_all = find_all_occurances(numbers_list, number_to_find)
    print(find_all)
