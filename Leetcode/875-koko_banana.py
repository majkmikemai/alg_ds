import math


def piles_calculator(piles, val):
    result = 0
    for p in piles:
        result += math.ceil(p / val)

    return result


def minEatingSpeed(piles, h: int) -> int:
    left = 1  # has to be 1, as the slowest pace is 1 banana/hour
    right = max(piles)

    while left < right:
        mid = (left + right) // 2

        if piles_calculator(piles, mid) > h:
            left = mid + 1
        else:
            right = mid
    return left


if __name__ == "__main__":
    piles = [1, 2, 3, 4]
    h = 9
    a = minEatingSpeed(piles, h)
    print(a)
