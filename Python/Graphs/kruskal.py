'''
KRUSKAL's ALGORITHM

It finds the minimum spanning tree (MST)

* Undirected and connected graphs
'''


#### Union-find algorithm  ####
def find_parent(parent, i):
    if parent[i] == -1:
        return i
    return find_parent(parent, parent[i])

def union(parent, x_set, y_set):
    parent[x_set] = y_set
#############################

def order_per_weight(graph, num_vertices):
    weights = {}
    for i in range(num_vertices):
        for j in range(i, num_vertices):
            if graph[i][j] is not None:
                w = graph[i][j]
                if w not in weights:
                    weights[w] = []
                weights[w].append([i,j])
    
    return weights


# input graph as an 2D matrix
def kruskal(graph):
    global INF
    
    num_vertices = len(graph)
    mst_edges = []
    parent = [-1 for i in range(num_vertices)]

    weights = order_per_weight(graph, num_vertices)

    for w in sorted(weights.keys()):
        for edge in weights[w]:
            x_parent = find_parent(parent, edge[0])
            y_parent = find_parent(parent, edge[1])
            if x_parent != y_parent:
                mst_edges.append(edge)
                union(parent, x_parent, y_parent)
            # if the belong to the same subset, it means there is a cycle
    print(mst_edges)
graph = [
    [None, 4,None, None, None, None, None, 8, None],
    [4, None, 8, None, None, None, None, 11, None],
    [None, 8, None, 7, None, 4, None, None, 2],
    [None, None, 7, None, 9, 14, None, None, None],
    [None, None, None, 9, None, 10, None, None, None],
    [None, None, 4, 14, 10, None, 2, None, None],
    [None, None, None, None, None, 2, None, 1, 6],
    [8, 11, None, None, None, None, 1, None, 7],
    [None, None, None, None, None, None,6, 7, None]]


kruskal(graph)