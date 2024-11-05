import heapq


def lastStoneWeight(stones) -> int:
    max_heap = [-stone for stone in stones]

    heapq.heapify(max_heap)

    while len(max_heap) > 1:
        x = -heapq.heappop(max_heap)
        y = -heapq.heappop(max_heap)

        if x != y:
            y = y - x
            heapq.heappush(max_heap, y)
        else:
            continue
    return -max_heap[0]


if __name__ == "__main__":
    stones = [2, 7, 4, 1, 8, 1]
    lastStoneWeight(stones)
