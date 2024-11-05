def numIslands(self, grid: List[List[str]]) -> int:
    # down, up,right,left
    self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    self.rows, self.cols = len(grid), len(grid[0])
    visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
    island = 0

    def dfs(self, grid, r, c, visited):
        # Marks the current node
        visited[r][c] = True
        stack = [(r, c)]

        # for the current node, check all directions and mark visited + add to the stack
        while stack:
            r, c = stack.pop()
            for directions in self.directions:
                new_r = r + directions[0]
                new_c = c + directions[1]

                if (
                    0 <= new_r < self.rows
                    and 0 <= new_c < self.cols
                    and not visited[new_r][new_c]
                    and grid[new_r][new_c] == "1"
                ):
                    visited[new_r][new_c] = True
                    stack.append((new_r, new_c))

    for i in range(self.rows):
        for j in range(self.cols):
            if grid[i][j] == "1" and not visited[i][j]:
                island += 1
                dfs(grid, i, j, visited)
    return island
