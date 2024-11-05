def containsDuplicate(nums) -> bool:
    res = {}

    for num in nums:
        if num not in res:
            res[num] = 1
        else:
            res[num] += 1

    for num, dup in res.items():
        if dup > 1:
            return True

    return False


if __name__ == "__main__":
    nums = [2, 14, 18, 22, 22]
    a = containsDuplicate(nums)
    print(a)
