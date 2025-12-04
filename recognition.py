from itertools import permutations, combinations
from networkx import Graph


def admits_solution_with_two_colors(graph: Graph) -> bool:
    for ordering in permutations(graph.nodes):
        for coloring in colorings(graph.nodes, 2):
            if is_solution(graph, ordering, coloring):
                return True
    return False


def colorings(iterable, colors: int):
    if len(iterable) == 0:
        yield {}
    else:
        first, *rest = iterable
        for smaller in colorings(rest, colors):
            for color in range(1, colors + 1):
                yield {first: color} | smaller


def is_solution(graph: Graph, ordering, coloring) -> bool:
    return all(not is_forbidden_pattern(graph, coloring, u, v, w) for u, v, w in combinations(ordering, 3))


def is_forbidden_pattern(graph: Graph, coloring, u, v, w) -> bool:
    return graph.has_edge(u, w) and (coloring[u] == coloring[v] or coloring[v] == coloring[w]) 
        