from collections import defaultdict


def groupAnagrams(strs):
    hash = defaultdict(list)

    for word in strs:
        # Non optimized approach of sorting word to be used as key fir hashmap
        # sorted_word = "".join(sorted(word))
        # hash[sorted_word].append(word)

        count = [0] * 26
        for w in word:
            count[ord(w) - ord("a")] += 1

        hash[tuple(count)].append(word)

    return list(hash.values())


if __name__ == "__main__":
    strs = ["cab", "tin", "pew", "duh", "may", "ill", "buy", "bar", "max", "doc"]
    a = groupAnagrams(strs)
    print(a)
