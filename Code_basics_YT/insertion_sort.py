def insertion_sort(elements):
    for i in range(len(elements)):
        anchor = elements[i]
        j = i - 1

        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1
        elements[j + 1] = anchor

        sorted_sublist = elements[: i + 1]
        mid = (i + 1) // 2

        if (i + 1) % 2 == 0:
            median = (sorted_sublist[mid - 1] + sorted_sublist[mid]) / 2
            print(f"Median for an even sorted list {median}")

        else:
            print(f"Median for an uneven sorted list {sorted_sublist[mid]}")
    return elements


if __name__ == "__main__":
    elements = [2, 1, 5, 7, 2, 0, 5]
    e = insertion_sort(elements)
    print(e)
