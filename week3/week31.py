import math

def adjlist(n, edges, oriented=False):
    succ = [[] for i in range(n)]
    for (a, b) in edges:
        succ[a].append(b)
        if not oriented:
            succ[b].append(a)
    return succ

def distance(n,edges,i,j):
    if len(edges) == 0:
        return math.inf
    if i == j:
        return 0
    dist = [math.inf] * n
    dist[i] = 0
    todo = [i]
    succ = adjlist(n, edges)
    while todo != []:
        x = todo.pop(0)
        for y in succ[x]:
            if dist[y] == math.inf:
                dist[y] = dist[x] + 1
                todo.append(y)
    for a in dist:
        if a == math.inf:
            return math.inf
    max = dist[0]
    for b in dist:
        if b > max:
            max = b
    return max