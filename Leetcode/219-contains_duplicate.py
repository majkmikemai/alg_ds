def containsNearbyDuplicate(nums, k: int) -> bool:
    n = len(nums)
    hash = {}

    for R in range(n):
        if R - L + 1 > k:
            hash.remove(nums[R])
            L += 1

        if nums[R] in hash:
            return True

        hash.add(nums[R])


if __name__ == "__main__":
    arr = [1, 2, 3, 3, 1, 3]
    target = 2
    print(containsNearbyDuplicate(arr, target))
