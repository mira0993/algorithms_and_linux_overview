

INF = 9999999
def dijkstra(graph, start_vertex):
    global INF

    prev = {}
    dist = {}

    vertices = list(graph.keys())
    for v in vertices:
        prev[v] = None
        if v == start_vertex:
            dist[v] = 0
        else:
            dist[v] = INF

    while len(vertices) > 0:
        # Find minimum dist vertex
        min_vertex = -1
        for v in range(len(vertices)):
            if min_vertex == -1 or dist[vertices[min_vertex]] > dist[vertices[v]]:
                min_vertex = v
        min_vertex = vertices.pop(min_vertex)
        for n in graph[min_vertex].keys():
            new_dist = dist[min_vertex] + graph[min_vertex][n]
            if new_dist < dist[n]:
                dist[n] = new_dist
                prev[n] = v
    print('Distances:')
    print(dist)
    print('Prev')
    print(prev)

graph = {
    'BWI': {'JFK': 184, 'MIA': 946 , 'ORD': 621},
    'MIA': {'JFK': 1090, 'BWI': 946 , 'DFW': 1121, 'BOS':1258, 'LAX': 2342},
    'JFK': {'BWI': 184, 'ORD': 740, 'PVD': 144, 'BOS': 187},
    'PVD': {'ORD': 849, 'JFK': 144},
    'ORD': {'BOS': 867 ,'PVD': 849, 'JFK': 740, 'BWI':621, 'DFW':802, 'SFO':1846},
    'BOS': {'ORD': 867, 'SFO': 2704, 'JFK': 187, 'MIA': 1258},
    'DFW': {'SFO': 1464, 'LAX': 1235, 'ORD': 802, 'MIA': 1121, 'JFK': 1391},
    'SFO': {'LAX': 337, 'DFW': 464, 'ORD': 1846, 'BOS': 2704},
    'LAX': {'SFO': 337, 'DFW': 1235, 'MIA': 2342}
}


dijkstra(graph, 'BWI')