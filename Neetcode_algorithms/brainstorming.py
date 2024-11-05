from collections import defaultdict
# ord a = 80
# ord z = 106
# z = 106-80 = 26


def topKFrequent(nums, k: int):
    hash = {}

    for n in nums:
        if n not in hash:
            hash[n] = 1
        else:
            hash[n] += 1

    list(hash)
    return sorted_values[:k]


if __name__ == "__main__":
    strs = [1, 1, 1, 2, 2, 3]
    a = topKFrequent(strs, 2)
    print(a)

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
