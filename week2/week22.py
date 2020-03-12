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