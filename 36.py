def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]


graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: [4],
    4: []
}

result = topological_sort(graph)

print("Topological Sorting:", result)