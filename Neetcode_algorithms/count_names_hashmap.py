def count_names(names):
    name_counter = {}

    for name in names:
        if name not in name_counter:
            name_counter[name] = 1
        else:
            name_counter[name] += 1
    return name_counter


if __name__ == "__main__":
    names = ("alice", "brad", "collin", "brad", "dylan", "kim")
    a = count_names(names)
    print(a)
