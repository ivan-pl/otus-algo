from typing import TypeAlias

Graph: TypeAlias = list[list[int]]


def kosaraju(graph: Graph) -> list[int]:
    pass


if __name__ == "__main__":
    graph: Graph = [
        [1],
        [2, 4, 5],
        [3, 6],
        [2, 7],
        [0, 5],
        [6],
        [5],
        [3, 6]
    ]
    components = kosaraju(graph)
    expected_components: graph = [0, 0, 1, 1, 0, 2, 2, 1]
    print('Result:\t', components)
    print('Expected:\t', expected_components)
