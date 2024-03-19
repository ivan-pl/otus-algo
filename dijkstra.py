from typing import TypeAlias, NamedTuple


class Edge(NamedTuple):
    v1: int
    v2: int


class VertexState(NamedTuple):
    w: int | None
    route: list[Edge]


AdjacencyMatrix: TypeAlias = list[list[int | None]]


def find_min_weight(vertices: dict[int, VertexState]) -> int:
    min_vertex = next(iter(vertices))
    min_weight = vertices[min_vertex].w
    for vertex, state in vertices.items():
        if state.w < min_weight:
            min_weight = state.w
            min_vertex = vertex
    return min_vertex


def dijkstra_full(graph: AdjacencyMatrix, start: int) -> dict[int, VertexState]:
    visited_vertices = set()
    shortest_routes: dict[int, VertexState] = {}
    vertices_current_state: dict[int, VertexState] = {start: VertexState(w=0, route=[])}

    while len(vertices_current_state) > 0:
        current_vertex = find_min_weight(vertices_current_state)
        visited_vertices.add(current_vertex)
        shortest_routes[current_vertex] = vertices_current_state[current_vertex]
        for adjacency, weight in enumerate(graph[current_vertex]):
            if weight is None or adjacency in visited_vertices:
                continue
            new_weight = vertices_current_state[current_vertex].w + weight
            if adjacency in vertices_current_state:
                if vertices_current_state[adjacency].w < new_weight:
                    continue
            new_route = vertices_current_state[current_vertex].route + [Edge(current_vertex, adjacency)]
            vertices_current_state[adjacency] = VertexState(w=new_weight, route=new_route)
        del vertices_current_state[current_vertex]

    return shortest_routes


def dijkstra_find_route(graph: AdjacencyMatrix, start: int, end: int) -> list[Edge] | None:
    visited_vertices = set()
    vertices_current_state: dict[int, VertexState] = {start: VertexState(w=0, route=[])}

    while len(vertices_current_state) > 0:
        current_vertex = find_min_weight(vertices_current_state)
        if current_vertex == end:
            return vertices_current_state[current_vertex].route
        visited_vertices.add(current_vertex)
        for adjacency, weight in enumerate(graph[current_vertex]):
            if weight is None or adjacency in visited_vertices:
                continue
            new_weight = vertices_current_state[current_vertex].w + weight
            if adjacency in vertices_current_state:
                if vertices_current_state[adjacency].w < new_weight:
                    continue
            new_route = vertices_current_state[current_vertex].route + [Edge(current_vertex, adjacency)]
            vertices_current_state[adjacency] = VertexState(w=new_weight, route=new_route)
        del vertices_current_state[current_vertex]

    return None


if __name__ == "__main__":
    graph: AdjacencyMatrix = [
        [None, 3, None, None, None, None, 2],
        [3, None, 1, None, 1, 2, None],
        [None, 1, None, 5, None, None, None],
        [None, None, 5, None, None, 1, None],
        [None, 1, None, None, None, 3, 2],
        [None, 2, None, 1, 3, None, 1],
        [2, None, None, None, 2, 1, None],
    ]

    shortest_routes = dijkstra_full(graph, 0)
    print(shortest_routes)

    edges = dijkstra_find_route(graph, 0, 3)
    print(edges)
