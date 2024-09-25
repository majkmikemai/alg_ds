def shell_sort(arr):
    size = len(arr)
    gap = size // 2

    while gap > 0:
        i = gap  # 3-9
        while i < size:
            anchor = arr[i]
            j = i

            while j >= gap and arr[j - gap] > anchor:
                arr[j] = arr[j - gap]
                j -= gap

            if j >= gap and arr[j - gap] == anchor:
                del arr[i]
                size -= 1
            else:
                arr[j] = anchor
                i += 1

        gap = gap // 2


if __name__ == "__main__":
    elements = [
        2,
        1,
        5,
        7,
        2,
        0,
        5,
        1,
        2,
        9,
        5,
        8,
        3,
    ]  # [21, 38, 29, 17, 4, 25, 11, 32, 9]
    shell_sort(elements)
    print(elements)
