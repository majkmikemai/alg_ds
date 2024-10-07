def search(nums, target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target < nums[mid]:
            if right - left <= 1:
                return mid
            else:
                right = mid - 1
        elif target > nums[mid]:
            if right - left < 1:
                return mid + 1
            else:
                left = mid + 1
        else:
            return mid
    return -1


if __name__ == "__main__":
    nums = [3, 5, 7, 9, 10]
    target = 8
    result = search(nums, target)
    print(result)
