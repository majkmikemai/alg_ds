def characterReplacement(s: str, k: int) -> int:
    n = len(s)
    L = 0
    hash = {}
    length = 0
    max_count = 0
    for R in range(n):
        hash[s[R]] = 1 + hash.get(s[R], 0)
        max_count = max(max_count, hash[s[R]])

        if R - L + 1 - max_count > k:
            hash[s[L]] -= 1
            L += 1

        length = max(length, R - L + 1)
    return length


if __name__ == "__main__":
    s = "AAAA"
    k = 0

    print(characterReplacement(s, 2))
