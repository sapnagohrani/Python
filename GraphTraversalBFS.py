def bfs(graph, vertex):
    visited = {vertex: True}
    queue = [vertex]
    level = {vertex: 0}

    while queue:
        v = queue.pop(0)
        for n in graph[v]:
            if n not in visited:
                queue.append(n)
                visited[n] = True
                level[n] = level[v]+1
    return visited, level


star = {
    'A': set(['D', 'E']),
    'B': set(['C', 'E']),
    'C': set(['B', 'D']),
    'D': set(['A', 'C']),
    'E': set(['A', 'B']),
}

traversed_vertices, distance = bfs(star, 'A')
print(traversed_vertices)
print(distance)