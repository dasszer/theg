import math

def make_weights_matrix(n, edges, e_plus, e_times):
    mat = [[e_plus for i in range(n)] for i in range(n)]
    for a, b, w in edges:
        mat[a][b] = w
    for k in range(n):
        mat[k][k] = e_times
    return mat

def floyd_warshall(n, edges, op_plus, e_plus, op_times, e_times):
    weights = make_weights_matrix(n,edges, e_plus, e_times)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                weights[i][j] = op_plus(weights[i][j], op_times(weights[i][k], weights[k][j]))
    return weights