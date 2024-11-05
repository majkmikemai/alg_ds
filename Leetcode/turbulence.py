def maxTurbulenceSize(arr) -> int:
    global_max = 1
    curr_max = 0
    L = 0

    if len(arr) <= 1:
        return len(arr)
    for R in range(1, len(arr) - 1):
        if arr[R] > arr[R - 1]:
            curr_max += 1
            global_max = max(curr_max, global_max)
        elif arr[R] < arr[R - 1]:
            curr_max += 1
            global_max = max(curr_max, global_max)
        elif arr[R] == arr[R - 1]:
            curr_max = 0
            global_max = max(curr_max, global_max)
            L = R - 1
        else:
            L = R - 1
    return global_max

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 5
    4   3
        2   1       
            1   0   1+0


if __name__ == "__main__":
    # arr = [4, 8, 12, 16]
    arr = [0, 1, 1, 0, 1, 0, 1, 1, 0, 0]
    a = maxTurbulenceSize(arr)
    print(a)
