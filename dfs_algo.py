def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result.append(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return result


G = {
    "a": set(["b", "c"]),
    "b": set(["a", "d"]),
    "c": set(["a", "d"]),
    "d": set(["e"]),
    "e": set(["a"])
}
result = []
marked: list = [False] * len(G)
res = dfs(G, "a")
print(*res)
