def lomuto_partition(elements, start, end):
    pivot = elements[end]

    i = start - 1

    for j in range(start, end):
        if elements[j] <= pivot:
            i += 1
            elements[i], elements[j] = elements[j], elements[i]

    elements[i + 1], elements[end] = elements[end], elements[i + 1]

    return i + 1


def hoare_partition(elements, start, end):
    pivot = elements[start]

    i = start
    j = end
    while i < j:
        if elements[i] <= pivot:
            i += 1

        elif elements[j] > pivot:
            j -= 1
        else:
            elements[j], elements[i] = elements[i], elements[j]
            i += 1
            j -= 1
    elements[start], elements[j] = elements[j], elements[start]

    return j


def quick_sort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        p_idx = lomuto_partition(elements, start, end)

        quick_sort(elements, start, p_idx - 1)
        quick_sort(elements, p_idx + 1, end)

    return elements


if __name__ == "__main__":
    elements = [11, 9, 29, 7, 2, 15, 28]
    qs = quick_sort(elements, 0, len(elements) - 1)
