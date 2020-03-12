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