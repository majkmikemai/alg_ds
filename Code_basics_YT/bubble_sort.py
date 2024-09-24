def bubble_sort(elements):
    size = len(elements)
    for j in range(size - 1):
        for i in range(size - 1):
            if elements[i] > elements[i + 1]:
                tmp = elements[i]
                elements[i] = elements[i + 1]
                elements[i + 1] = tmp
    return elements


if __name__ == "__main__":
    elements = [4, 1, 3, 2]

    bubble = bubble_sort(elements)
    print(bubble)
