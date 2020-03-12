def check_correct_path(n,edges,path):
    correct = 0
    index = 0
    while (index < len(path) - 1):
        for b,c,d in edges:
            if path[index] == b and path[index + 1] == c:
                correct = correct + 1
        index = index + 1
    if correct == len(path) - 1:
        return True
    else:
        return False

def find_path_distance(n,edges,path):
    if check_correct_path(n,edges,path) == False:
        return None
    dist = 0
    index = 0
    while (index < len(path) - 1):
        for b,c,d in edges:
            if path[index] == b and path[index + 1] == c:
                dist = dist + d
                break
        index = index + 1
    return dist

edges = [(0,1,1),(0,3,1),(0,4,4),(1,2,2),(1,4,3),(2,5,1),(3,4,2),(4,5,-2),(5,2,-1)]
print(find_path_distance(6,edges,[0,4,5])) #2

edges = [(0,1,1),(0,3,1),(0,4,4),(1,2,2),(1,4,3),(2,5,1),(3,4,2),(4,5,-2),(5,2,-1)]
print(find_path_distance(6,edges,[0,4,3])) #None

edges = [(0,1,1),(0,3,1),(0,4,4),(1,2,2),(1,4,3),(2,5,1),(3,4,2),(4,5,-2),(5,1,-1)]
print(find_path_distance(6,edges,[1,2,5,1,4,5,1,2,5])) #5
	
edges = [(0,1,1),(0,3,1),(0,4,4),(1,2,2),(1,4,3),(2,5,1),(3,4,2),(4,5,-2),(5,1,-1)]
print(find_path_distance(6,edges,[1,2,5,1,4,5,1,2,5,3,0,1])) #None