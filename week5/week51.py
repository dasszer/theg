from collections import defaultdict

def is_connected(n,edges,src,dest):
    visited = [False] * n
    queue = []
    queue.append(src)
    visited[src] = True
    while queue:
        n = queue.pop(0)
        if n == dest:
            return True
        for i in edges[n]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    return False

def connected_to(n,edges,src):
    if (len(edges) == 0 | n == 0):
        return []
    edges_dico = defaultdict(list)

    for a,b in edges:
        edges_dico[a].append(b)
        edges_dico[b].append(a)

    vertices = []
    for i in range(n):
        if (is_connected(n,edges_dico,src,i) == True):
            vertices.append(i)

    return vertices