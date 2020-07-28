def bfs(graph, vertex):
    visited = {vertex: True}
    queue = [vertex]

    while queue:
        v = queue.pop(0)
        for n in graph[v]:
            if n not in visited:
                queue.append(n)
                print(queue)
                visited[n] = True
    return visited


star = {
    'A': set(['D', 'E']),
    'B': set(['C', 'E']),
    'C': set(['B', 'D']),
    'D': set(['A', 'C']),
    'E': set(['A', 'B']),
}

traversed_vertices = bfs(star, 'A')
print(traversed_vertices)