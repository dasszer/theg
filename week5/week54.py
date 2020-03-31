import math

def make_weights_matrix(n, edges, e_plus, e_times):
    mat = [[e_plus for i in range(n)] for i in range(n)]
    for a, b, w in edges:
        mat[a][b] = w
    for k in range(n):
        mat[k][k] = e_times
    return mat

def find_path(n, edges, src, dst):
    dist = [math.inf] * n
    dist[src] = 0
    parent = list(range(n))
    for k in range(n - 1):
        for (s, d, w) in edges:
            if dist[d] < dist[s] + w:
                parent[d] = s
                dist[d] = dist[s] + w
    
    if dist[dst] == math.inf:
        return []

    sp = [dst]
    while dst != src:
        dst = parent[dst]
        sp.insert(0, dst)
    return sp

def safest_path(n,edges,source,destination):
    if source == destination:
        return [source]
    return find_path(n, edges, source, destination)