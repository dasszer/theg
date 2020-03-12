def odd_vertices(n, edges):
    odd = []
    i = 0
    while i <= n:
        count = 0
        for j, k in edges:
            if j == i:
                count = count + 1
            if k == i:
                count = count + 1
        if count % 2 == 1:
            odd.append(i)
        i = i + 1
    return odd

def is_edge_connected(n, edges):
    if len(edges) == 0:
        return True
    ind = 0
    for k, l in edges:
        if k == l:
            edges.pop(ind)
            n = n - 1
        ind = ind + 1
    j = 0
    while j < n:
        nexist = False
        for a, b in edges:
            if n - j - 1 == a or n - j - 1 == b:
                nexist = True
        if nexist == False:
            index = 0
            for a, b in edges:
                deca = 0
                decb = 0
                if a > n - j - 1:
                    deca = 1
                if b > n - j - 1:
                    decb = 1
                edges.pop(index)
                edges.insert(index, (a-deca, b-decb))
                index = index + 1
            n = n - 1
        j = j + 1
    i = 0
    good_vertices =[]
    while i < n:
        if has_path(0, i, edges, good_vertices) == False:
            return False
        good_vertices.append(i)
        i = i + 1
    return True
    
def has_path(start, end, edges, good_vertices):
    if start == end:
        return True
    for a in good_vertices:
        for b, c in edges:
            if a == b and c == end:
                return True
            if a == c and b == end:
                return True
    return False

def is_eulerian(n, edges):
    if not odd_vertices(n, edges) and is_edge_connected(n, edges) == True:
        return True
    return False

def find_eulerian_cycle(m, edges):
    if is_eulerian(m, edges) == False:
        return []
    if len(edges) == 0:
        return []
    cycle = []
    other = []
    cycle.append(edges[0][0])
    while 1:
        other = []
        for a, b in edges:
            if cycle[len(cycle) - 1] == a:
                cycle.append(b)
            elif cycle[len(cycle) - 1] == b:
                cycle.append(a)
            else:
                other.append((a, b))
        if other == []:
            if cycle[len(cycle) - 1] != cycle[0]:
                return []
            else:
                return cycle[0:len(cycle) - 1]
        else:
            edges = other
            if cycle[len(cycle) - 1] == cycle[0]:
                for c, d in other:
                    if c in cycle:
                        i = cycle.index(c)
                        cycle = cycle[i:len(cycle) - 1] + cycle[0:i+1]