from collections import defaultdict
import heapq
import math

def find_shortest_distance(edges_dico,src,dest):
    if src == dest:
        return 0

    q = [(0, src, [])]
    visit = set()
    heapq.heapify(q)

    while q:
        (weight, elem, path) = heapq.heappop(q)
        if elem not in visit:
            visit.add(elem)
            path = path + [elem]

            if elem == dest:
                return path

            for nextelem, moreweight in edges_dico[elem]:
                if nextelem not in visit:
                    heapq.heappush(q, (weight+moreweight, nextelem, path))

def shortest_path(n,edges,src,dest):
    edges_dico = defaultdict(list)

    for a,b,c in edges:
        edges_dico[a].append((b,c))

    dist = [math.inf] * n
    dist[src] = 0

    for i in range(n - 1):
        for (a,b,c) in edges:
            dist[b] = min(dist[b], dist[a] + c)

    for a,b,c in edges:
        if dist[b] > dist[a] + c:
            return None

    return find_shortest_distance(edges_dico,src,dest)