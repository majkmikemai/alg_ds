class Heap:
    def __init__(self) -> None:
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        print(i)

        while self.heap[i] < self.heap[i // 2]:
            # Percolate up
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i //= 2
        print(self.heap)

    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]

        i = 1
        self.heap[1] = self.heap.pop()
        while 2 * i < len(self.heap):
            if (
                2 * i + 1 < len(self.heap)
                and self.heap[2 * i + 1] < self.heap[2 * i]
                and self.heap[2 * i + 1] < self.heap[i]
            ):
                self.heap[2 * i + 1], self.heap[i] = (
                    self.heap[i],
                    self.self.heap[2 * i + 1],
                )
                i = 2 * 1 + 1
            elif self.heap[2 * i] < self.heap[i]:
                self.heap[2 * i], self.heap[i] = self.heap[i], self.self.heap[2 * i]
                i *= 2
            else:
                break
        return res


if __name__ == "__main__":
    a = Heap()
    a.push(4)
    print(a.heap[1])
