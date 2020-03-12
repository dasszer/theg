def is_connected(n, edges):
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