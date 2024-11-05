def brute_force_sliding(arr, k):
    n = len(arr)

    for L in range(n):
        for R in range(L + 1, min(n, L + k)):
            if arr[L] == arr[R]:
                return True
    return False


def closeDuplicates(nums, k):
    window = set()  # Cur window of size <= k
    L = 0

    for R in range(len(nums)):
        if R - L + 1 >= k:
            if nums[R] in window:
                return True
            window.remove(nums[L])
            L += 1
        window.add(nums[R])

    return False


if __name__ == "__main__":
    arr = [2, 3, 2, 3, 3]
    print(brute_force_sliding(arr, 2))
