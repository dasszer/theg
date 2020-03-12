def is_simple(n, edges):
    for i, j in edges:
        for k, l in edges:
            if i == l and j == k:
                return False
    return True