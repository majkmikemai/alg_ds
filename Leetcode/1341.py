def search(arr, k, threshold):
    n = len(arr)

    L = 0
    res = 0
    curr_sum = 0

    for R in range(n):
        curr_sum += arr[R]

        if R - L + 1 == k:
            if curr_sum / 3 >= threshold:
                res += 1
            curr_sum -= arr[L]
            L += 1
    return res


if __name__ == "__main__":
    arr = [2, 2, 3, 2, 5, 5, 5, 8]
    k = 3
    threshold = 4
    print(search(arr, k, threshold))
