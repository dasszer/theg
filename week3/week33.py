def create_adjmatrix(n, edges):
    mat = [[0 for i in range(n)] for i in range(n)]
    for a, b in edges:
        mat[a][b] = 1
        mat[b][a] = 1
    return mat
  
def chap_count_k_step_walks(n, k, v1, v2, edges):
    cpt = 0  
    if (k == 0 and v1 == v2): 
        return 1
    if (k == 1 and edges[v1][v2]): 
        return 1
    if (k <= 0): 
        return 0
    for a in range(0, n): 
        if (edges[v1][a] == 1):  
            cpt += chap_count_k_step_walks(n, k - 1, a, v2, edges) 
    return cpt

def count_k_step_walks(n, k, v1, v2, edges):
    mat = create_adjmatrix(n, edges)
    return chap_count_k_step_walks(n, k, v1, v2, mat)