import math

def single_source_distances(n,edges,src):
    dist = [math.inf] * n
    dist[src] = 0

    for i in range(n - 1):
        for (a,b,c) in edges:
            dist[b] = min(dist[b], dist[a] + c)

    for a,b,c in edges:
        if dist[b] > dist[a] + c:
            return None

    return dist