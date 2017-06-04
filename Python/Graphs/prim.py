'''
PRIM ALGORITHM

It finds the minimum spanning tree (MST)

* Undirected and connected graphs
'''
INF = 99999999

# input graph as an 2D matrix

def prim(graph):
    global INF
    
    num_vertices = len(graph)
    key_values = {0:0}
    prev = {0:None}
    mst = []

    for i in range(1, num_vertices):
        key_values[i] = INF
        prev[i] = None
    
    while len(mst) < num_vertices:
        min_vertex = None

        for i in range(num_vertices):
            if (min_vertex is None or key_values[min_vertex] > key_values[i]) and i not in mst:
                min_vertex = i

        if min_vertex is None:
            print('Error found....')
            break

        mst.append(min_vertex)

        for j in range(num_vertices):
            if graph[min_vertex][j] is not None and graph[min_vertex][j] < key_values[j]:
                key_values[j] = graph[min_vertex][j]
                if j not in mst:
                    prev[j] = min_vertex

    print('Previous node path')
    print(prev)
    print(mst)

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


prim(graph)