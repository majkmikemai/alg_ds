def firstBadVersion(self, n: int) -> int:
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) //2

        if isBadVersion(mid):
            if right-left <= 1:
                return mid +1
            right = mid -1
        elif not isBadVersion(mid):
            left = mid +1
    return mid +1

if __name__ == "__main__":
    