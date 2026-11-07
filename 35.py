# Detect cycle in a directed graph
def directed_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True

    return False


# Detect cycle in an undirected graph
def undirected_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


# Directed graph
directed = {
    0: [1],
    1: [2],
    2: [0]
}

# Undirected graph
undirected = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print("Directed Graph:", "Cycle detected" if directed_cycle(directed) else "No cycle")
print("Undirected Graph:", "Cycle detected" if undirected_cycle(undirected) else "No cycle")