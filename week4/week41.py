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