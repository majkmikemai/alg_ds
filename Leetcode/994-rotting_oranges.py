from collections import deque


def orangesRotting(grid) -> int:
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    visited = [[False for _ in range(cols)] for _ in range(rows)]

    queue = deque()
    apples = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                apples += 1

    max_steps = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                visited[i][j] = True
                queue.append((i, j, max_steps))

                while queue:
                    r, c, step = queue.popleft()
                    for dir in directions:
                        new_r, new_c = r + dir[0], c + dir[1]
                        if (
                            0 <= new_r < rows
                            and 0 <= new_c < cols
                            and grid[new_r][new_c] == 1
                            and not visited[new_r][new_c]
                        ):
                            visited[new_r][new_c] = True
                            queue.append((new_r, new_c, step + 1))
                            apples -= 1
    if apples > 0:
        return -1
    else:
        return max_steps


if __name__ == "__main__":
    grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]

    print(orangesRotting(grid))
