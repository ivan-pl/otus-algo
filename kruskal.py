from typing import TypeAlias

AdjacencyVector: TypeAlias = list[list[tuple[int, int]]]


class Edge:
    def __init__(self, v1: int, v2: int, weight: int):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __repr__(self):
        return f'({self.v1},{self.v2},{self.weight})'


class Graph:
    def __init__(self, adjacency_vector: list[list[tuple[int, int]]]):
        self.adjacency_vector = adjacency_vector
        self.edges = []

    @staticmethod
    def _make_edges_by_adjacency_vector(adjacency_vector: AdjacencyVector) -> list[Edge]:
        pass

    def kruskal(self) -> list[Edge]:
        pass


if __name__ == "__main__":
    adjacency_vector: AdjacencyVector = [
        [(1, 3), (4, 4), (7, 3)],
        [(0, 3), (2, 4), (4, 3)],
        [(1, 4), (3, 2), (4, 1), (5, 3)],
        [(2, 2), (6, 3), (7, 2)],
        [(0, 4), (1, 3), (2, 1), (5, 2), (6, 4), (7, 2)],
        [(2, 3), (4, 2)],
        [(4, 4), (3, 3)],
        [(0, 3), (3, 2), (4, 2)]
    ]

    graph = Graph(adjacency_vector)
    edges = graph.kruskal()
    print('Result\n', edges)
