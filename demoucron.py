from typing import TypeAlias

Matrix: TypeAlias = list[list[int | None]]
Level: TypeAlias = list[int | None]


def vector_to_matrix(vector: list[list[int]]) -> Matrix:
    n = len(vector)
    matrix: Matrix = [[None] * n for i in range(n)]
    for i, row in enumerate(vector):
        for vertex in row:
            matrix[i][vertex] = 1
    return matrix


def get_level_from_matrix(matrix: Matrix) -> list[int]:
    cur_level = [0] * len(matrix[0])
    for col in range(len(matrix[0])):
        total = 0
        for row in range(len(matrix)):
            if matrix[row][col]:
                total += 1
        if total:
            cur_level[col] = total
    return cur_level


def demoucron(vector: list[list[int]]) -> Matrix:
    matrix = vector_to_matrix(vector)
    levels: Matrix = []

    cur_level = get_level_from_matrix(matrix)
    while any(num is not None for num in cur_level):
        levels.append(cur_level)
        zero_vertexes = [i for i, inc_connections in enumerate(cur_level) if inc_connections == 0]
        zero_vertex_level = get_level_from_matrix([matrix[i] for i in zero_vertexes])
        next_level = [None] * len(matrix)
        for i, inc_connections in enumerate(cur_level):
            if inc_connections:
                next_level[i] = inc_connections if not zero_vertex_level[i] else inc_connections - zero_vertex_level[i]
        cur_level = next_level

    return levels


if __name__ == "__main__":
    vector = [
        [1],
        [4],
        [3],
        [0, 1, 4, 5],
        [6],
        [4, 7],
        [7],
        []
    ]
    levels = demoucron(vector)
    print(levels)
