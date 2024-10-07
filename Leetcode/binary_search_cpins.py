def arrangeCoins(n: int) -> int:
    result = 0
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2

        # Gaussian formula
        coins = (mid / 2) * (mid + 1)

        if coins > n:
            right = mid - 1

        else:
            left = mid + 1
            result = mid
    return result


if __name__ == "__main__":
    n = 5
    a = arrangeCoins(n)
    print(a)
