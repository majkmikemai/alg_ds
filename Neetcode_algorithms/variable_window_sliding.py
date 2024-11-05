# find the length of the longest subarray with the same value in each position
def searching_(arr):
    n = len(arr)

    L = 0
    dup = set()
    dup.add(arr[0])
    res = 1
    curr_sum = 1

    for R in range(n):
        if arr[R] not in dup:
            dup.remove(arr[L])
            L += 1
            curr_sum = 1
        else:
            curr_sum += 1

        dup.add(arr[R])
        res = max(curr_sum, res)
    return res


if __name__ == "__main__":
    arr = [4, 2, 2, 3, 3, 3]
    print(searching_(arr))
