# The number of vertices
nV = 4

INF = 999


# Algorithm implementation
def floyd_warshall(G):
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                if i != k and j != k and i != j:
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j])  # Formula for calculating
    return G


G = [[0, 3, INF, 5], [2, 0, INF, 4], [INF, 1, 0, INF], [INF, INF, 2, 0]]

print(floyd_warshall(G))

