from typing import TypeAlias
import queue

Graph: TypeAlias = list[list[int]]


def inverse_graph(graph: Graph) -> Graph:
    new_graph: graph = [[] for i in range(len(graph))]
    for vertex, adjacent_vertexes in enumerate(graph):
        for adjacent_vertex in adjacent_vertexes:
            new_graph[adjacent_vertex].append(vertex)
    return new_graph


def dfs_back_route(graph: Graph) -> list[int]:
    visited: set[int] = set()
    added_in_route: set[int] = set()
    back_route: list[int] = []
    vertex_stack: list[int] = list(range(len(graph)))

    while vertex_stack:
        cur_vertex = vertex_stack[-1]
        if cur_vertex in visited:
            vertex_stack.pop()
            if cur_vertex not in added_in_route:
                back_route.append(cur_vertex)
                added_in_route.add(cur_vertex)
            continue

        visited.add(cur_vertex)
        for adjacent_vertex in graph[cur_vertex]:
            if adjacent_vertex in visited:
                continue
            vertex_stack.append(adjacent_vertex)

    return back_route


def dfs(graph: Graph, start: int, visited: set[int]) -> list[int]:
    vertex_stack = queue.LifoQueue()
    route: list[int] = [start]
    for adjacent_vertex in graph[start]:
        if adjacent_vertex not in visited:
            vertex_stack.put(adjacent_vertex)

    visited.add(start)
    while not vertex_stack.empty():
        vertex = vertex_stack.get()
        route.append(vertex)
        visited.add(vertex)
        for adjacent_vertex in graph[vertex]:
            if adjacent_vertex not in visited:
                vertex_stack.put(adjacent_vertex)

    return route


def kosaraju(graph: Graph) -> list[int]:
    inversed_graph = inverse_graph(graph)
    route: list[int] = dfs_back_route(inversed_graph)
    route.reverse()

    visited: set[int] = set()
    components: list[list[int]] = []
    for vertex in route:
        if vertex in visited:
            continue

        components.append(dfs(graph, vertex, visited))

    result: list[int] = [0] * len(graph)
    for ind, component in enumerate(components):
        for vertex in component:
            result[vertex] = ind

    return result


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
