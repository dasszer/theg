import math

def make_weights_matrix(n, edges, e_plus, e_times):
    mat = [[e_plus for i in range(n)] for i in range(n)]
    for a, b, w in edges:
        mat[a][b] = w
    for k in range(n):
        mat[k][k] = e_times
    return mat

def find_path(n, edges, plus, e_plus, times, e_times, src, dst):
    dist = [e_plus] * n
    dist[src] = e_times
    parent = list(range(n))
    for k in range(n - 1):
        for (s, d, w) in edges:
            if plus(dist[d], times(dist[s], w)) != dist[d]:
                parent[d] = s
                dist[d] = times(dist[s], w)
    
    if dist[dst] == e_plus:
        return []

    sp = [dst]
    while dst != src:
        dst = parent[dst]
        sp.insert(0, dst)
    return sp


def floyd_warshall(n, edges, plus, e_plus, times, e_times):
    weights = make_weights_matrix(n,edges, e_plus, e_times)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                weights[i][j] = plus(weights[i][j], times(weights[i][k], weights[k][j]))
    return weights, [n, edges, plus, e_plus, times, e_times]


def path(D,source,destination):
    if source == destination:
        return [source]
    return find_path(D[0], D[1], D[2], D[3], D[4], D[5], source, destination)


def op_min(a, b):
    return min(a, b)

def op_max(a, b):
    return max(a, b)

def op_add(a, b):
    return a+b

def op_sub(a, b):
    return a-b

	
n = 5
edges = [(0,1,1), (1,0,3), (3,2,1), (1,4,4), (4,3,-1), (3,4,2)]
M,D = floyd_warshall(n,edges,op_min, math.inf, op_add, 0)
print(M)
print(D)
n = 5
#edges = [(0,1,7), (1,0,3), (3,2,1), (1,4,4), (4,3,3), (3,4,2), (0,3,1)]
M,D = floyd_warshall(n,edges,op_max, 0, op_sub, math.inf)
print(M)
print(D)

#print (make_weights_matrix(n, edges, math.inf, 0))
#print(path(D, 0, 0))
#print(path(D, 0, 1))
#print(path(D, 0, 2))
#print(path(D, 0, 3))
#print(path(D, 0, 4))
#print(path(D, 1, 0))
#print(path(D, 1, 1))
#print(path(D, 1, 2))
#print(path(D, 1, 3))
#print(path(D, 1, 4))
#print(path(D, 2, 0))
#print(path(D, 2, 1))
#print(path(D, 2, 2))
#print(path(D, 2, 3))
#print(path(D, 2, 4))
#print(path(D, 3, 0))
#print(path(D, 3, 1))
#print(path(D, 3, 2))
#print(path(D, 3, 3))
#print(path(D, 3, 4))
#print(path(D, 4, 0))
#print(path(D, 4, 1))
#print(path(D, 4, 2))
#print(path(D, 4, 3))
#print(path(D, 4, 4))
