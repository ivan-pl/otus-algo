from typing import TypeAlias
from random import randint

AdjacencyVector: TypeAlias = list[list[tuple[int, int]]]


class Edge:
    def __init__(self, v1: int, v2: int, weight: int):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def items(self):
        return self.v1, self.v2, self.weight

    def __repr__(self):
        return f'({self.v1},{self.v2},{self.weight})'


class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]

    def find(self, i: int) -> int:
        if self.parents[i] == i:
            return i

        return self.find(self.parents[i])

    def unite(self, a: int, b: int) -> None:
        main_a = self.find(a)
        main_b = self.find(b)
        if randint(0, 1) == 0:
            self.parents[main_a] = main_b
        else:
            self.parents[main_b] = main_a


class Graph:
    def __init__(self, adjacency_vector: list[list[tuple[int, int]]]):
        self.adjacency_vector = adjacency_vector
        self.edges = Graph._make_edges_by_adjacency_vector(adjacency_vector)
        self.edges.sort(key=lambda x: x.weight)

    @staticmethod
    def _make_edges_by_adjacency_vector(adjacency_vector: AdjacencyVector) -> list[Edge]:
        edges: list[Edge] = []
        for vertex1, adjacency in enumerate(adjacency_vector):
            for vertex2, weight in adjacency:
                if vertex2 > vertex1:
                    edges.append(Edge(vertex1, vertex2, weight))
        return edges

    def kruskal(self) -> list[Edge]:
        union_find = UnionFind(len(self.adjacency_vector))
        min_skeleton: list[Edge] = []
        for edge in self.edges:
            v1, v2, weight = edge.items()
            if union_find.find(v1) != union_find.find(v2):
                union_find.unite(v1, v2)
                min_skeleton.append(edge)
            if len(min_skeleton) >= len(adjacency_vector) - 1:
                break
        return min_skeleton


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
    print(edges)
