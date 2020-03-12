from collections import defaultdict
import heapq

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
                return weight

            for nextelem, moreweight in edges_dico[elem]:
                if nextelem not in visit:
                    heapq.heappush(q, (weight+moreweight, nextelem, path))
    
def single_source_distances(n,edges,src):
    if (len(edges) == 0 | n == 0):
        return []
    edges_dico = defaultdict(list)

    for a,b,c in edges:
        edges_dico[a].append((b,c))
        edges_dico[b].append((a,c))

    weights = []
    for i in range(n):
        weights.append(find_shortest_distance(edges_dico,src,i))

    for weight in weights:
        if weight < 0:
            return None
    return weights


edges = [(0,1,1),(2,1,2),(2,0,4)]
print(single_source_distances(3,edges,0))

edges = [(0,3,2),(0,1,1),(1,2,12),(2,0,-3)]
print(single_source_distances(4,edges,0))