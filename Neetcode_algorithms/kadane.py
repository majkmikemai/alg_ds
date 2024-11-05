# Bruteforce


def bruteforce(nums):
    max_sum = nums[0]

    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]

            max_sum = max(max_sum, curr_sum)
    return max_sum


nums = [4, -1, 2, -7, 3, 4]
bruteforce(nums)


def kadanes(nums):
    max_sum = nums[0]
    curr_sum = 0

    for i, n in enumerate(nums):
        curr_sum = max(curr_sum, 0)
        curr_sum += n
        print(f"current Sum {curr_sum} at index", i)
        max_sum = max(curr_sum, max_sum)
    return max_sum


kadanes(nums)


def sliding_window(nums):
    max_sum = nums[0]
    curr = 0

    max_left, max_right = 0, 0

    left = 0

    for right in range(len(nums)):
        if curr < 0:
            curr = 0

            left = right
            print(left)
        curr += nums[right]

        if curr > max_sum:
            max_sum = curr
            max_left, max_right = left, right
    return [max_left, max_right]


sliding_window(nums)
