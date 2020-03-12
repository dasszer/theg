from collections import defaultdict

def is_eulerian_cycle(m, edges, cycle):
    if len(edges) != len(cycle):
        return False
    if len(edges) == 0:
        return True
    lista = {}
    for a, b in edges:
        c = 0
        if a < b:
            c = (a, b)
        else:
            c = (b, a)
        if c in lista:
            lista[c] = lista[c] + 1
        else:
            lista[c] = 1
    i = 0
    listb = []
    while i + 1 < len(cycle):
        listb.append((cycle[i], cycle[i + 1]))
        i = i + 1
    listb.append((cycle[0], cycle[len(cycle) - 1]))
    for x, y in listb:
        z = 0
        if x < y:
            z = (x, y)
        else:
            z = (y, x)
        if z in lista:
            lista[z] = lista[z] - 1
        else:
            return False
    for e in lista.values():
        if e != 0:
            return False
    return True

def check_contradictory(n, constraints):
    for a,b in constraints:
        for c,d in constraints:
            for e,f in constraints:
                if (a == d or a == f) and (c == b or c == e) and (e == b or e == d):
                    return False

def chap_topological_sort(v, constraints, visit, ret):
    visit[v] = True
    for i in constraints[v]:
        if visit[i] == False:
            chap_topological_sort(i, constraints, visit, ret)
    ret.insert(0, v)

def is_topological_order(n,constraints,permutation):
    if (len(permutation) == 0 | len(constraints) == 0 | n == 0):
        return False
    if (len(permutation) != n):
        return False
    for a,b in constraints:
        left = 0
        right = 0
        pos = 0
        for c in permutation:
            if a == c:
                left = pos
            if b == c:
                right = pos
            pos = pos + 1
        if left >= right:
            return False
    return True
    
def topological_sort(n,constraints):
    if (n == 0):
        return False
    if (check_contradictory(n, constraints) == False):
        return False
    if is_eulerian_cycle(n,constraints,[i for i in range(n)]) == True:
        return False
    if constraints == []:
        return [i for i in range(n)]
    visit = [False] * n
    ret = []
    newconstraints = defaultdict(list)
    for a,b in constraints:
        newconstraints[a].append(b)
    for i in range(n):
        if visit[i] == False:
            chap_topological_sort(i, newconstraints, visit, ret)
    if is_topological_order(n, constraints, ret) == False:
        return False
    return ret