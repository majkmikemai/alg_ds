def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
    rows, cols = len(game_matrix), len(game_matrix[0])

    directions_steps = [(0, -1, 1), (0, 1, 2), (1, 0, 1), (-1, 0, 1)]

    def dfs(r, c, ds):
        new_r, new_c, max_steps = ds[0], ds[1], ds[2]
        steps = 0
        while (
            0 <= r < rows and 0 <= c < cols and game_matrix[r][c] and steps <= max_steps
        ):
            if (r, c) == (to_row, to_column):
                return True
            else:
                r = r + new_r
                c = c + new_c
                steps += 1
        return False

    for ds in directions_steps:
        if dfs(from_row, from_column, ds):
            return True

    return False


if __name__ == "__main__":
    gameMatrix = [
        [False, True, True, False, False, False],
        [True, True, True, False, False, False],
        [True, True, True, True, True, True],
        [False, True, True, False, True, True],
        [False, True, True, True, False, True],
        [False, False, False, False, False, False],
    ]

    print(can_travel_to(gameMatrix, 3, 2, 2, 2))  # True, Valid move
    print(can_travel_to(gameMatrix, 3, 2, 3, 4))  # False, Can't travel through land
    print(can_travel_to(gameMatrix, 3, 2, 6, 2))  # False, Out of bounds


# def can_travel_to(game_matrix, from_row, from_column, to_row, to_column):
#     # Custom movement rules: 1 step up, 1 step down, 1 step left, 1 or 2 steps right
#     directions = [
#         (-1, 0, 1),  # 1 step up
#         (1, 0, 1),  # 1 step down
#         (0, -1, 1),  # 1 step left
#         (0, 1, 2),  # 2 steps right
#     ]

#     rows, cols = len(game_matrix), len(game_matrix[0])

#     # Check if start and target are within bounds
#     if not (0 <= from_row < rows and 0 <= from_column < cols):
#         return False
#     if not (0 <= to_row < rows and 0 <= to_column < cols):
#         return False

#     # Use a visited matrix to avoid revisiting cells
#     visited = [[False for _ in range(cols)] for _ in range(rows)]

#     # Depth-first search with a limited number of steps
#     def dfs(r, c, dr, dc, max_steps):
#         steps = 0
#         # Traverse in the fixed direction, but only up to the allowed number of steps
#         while (
#             0 <= r < rows and 0 <= c < cols and game_matrix[r][c] and steps <= max_steps
#         ):
#             if (r, c) == (to_row, to_column):
#                 return True
#             visited[r][c] = True
#             r += dr
#             c += dc
#             steps += 1
#         return False

#     # Try moving in each of the constrained directions from the start point
#     for dr, dc, max_steps in directions:
#         if dfs(from_row, from_column, dr, dc, max_steps):
#             return True

#     return False


# if __name__ == "__main__":
#     gameMatrix = [
#         [False, True, True, False, False, False],
#         [True, True, True, False, False, False],
#         [True, True, True, True, True, True],
#         [False, True, True, False, True, True],
#         [False, True, True, True, False, True],
#         [False, False, False, False, False, False],
#     ]

#     print(can_travel_to(gameMatrix, 3, 2, 2, 2))  # True, Valid move
#     print(can_travel_to(gameMatrix, 3, 2, 3, 4))  # False, Can't travel through land
#     print(can_travel_to(gameMatrix, 3, 2, 6, 2))  # False, Out of bounds
