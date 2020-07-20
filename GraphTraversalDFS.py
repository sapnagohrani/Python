class Graph:
    def __init__(self, graph):
        self.graph = graph

    # Depth First Search Logic
    def dfs_traversal(self, vertex, visited_vertices=None):
        if visited_vertices is None:
            visited_vertices = set()
        visited_vertices.add(vertex)
        print(visited_vertices)
        for adjacent_vertex in self.graph[vertex] - visited_vertices:
            self.dfs_traversal(adjacent_vertex, visited_vertices)
        return visited_vertices


star = {
    'A': set(['D', 'E']),
    'B': set(['C', 'E']),
    'C': set(['B', 'D']),
    'D': set(['A', 'C']),
    'E': set(['A', 'B']),
}
graph = Graph(star)
graph.dfs_traversal('A')
