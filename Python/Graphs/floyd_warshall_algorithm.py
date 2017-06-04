'''
The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. 
The problem is to find shortest distances between every pair of vertices in a
given edge weighted directed Graph.

Input:
       graph[][] = { {0,   5,  INF, 10},
                    {INF,  0,  3,  INF},
                    {INF, INF, 0,   1},
                    {INF, INF, INF, 0} }
which represents the following graph
             10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3       
Note that the value of graph[i][j] is 0 if i is equal to j 
And graph[i][j] is INF (infinite) if there is no edge from vertex i to j.

Output:
Shortest distance matrix
      0      5      8      9
    INF      0      3      4
    INF    INF      0      1
    INF    INF    INF      0 

Floyd Warshall Algorithm
1. Initialize the solution matrix same as the input graph matrix as a first step. 
2. Update the solution matrix by considering all vertices as an intermediate vertex.
   The idea is to one by one pick all vertices and update all shortest paths which include the picked vertex as
   an intermediate vertex in the shortest path.
   For every pair (i, j) of source and destination vertices respectively, there are two possible cases.
     2.1) k is not an intermediate vertex in shortest path from i to j. Keep the value of dist[i][j] as it is.
     2.2) k is an intermediate vertex in shortest path from i to j. Update the value of dist[i][j] as dist[i][k] + dist[k][j].
'''

# Number to represent infinite
INF = 999999

graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

def floydWarshall(graph, num_vertices):

    shortestDistances = []
    for v in range(num_vertices):
        shortestDistances.append(list(graph[v]))
    

    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # If vertex k is on the shortest path from 
                # i to j, then update the value of dist[i][j]
                shortestDistances[i][j] = min(shortestDistances[i][j],
                                              shortestDistances[i][k]+ shortestDistances[k][j])
    print(shortestDistances)

def print_graph(graph):
    for i in graph:
        print(i)


floydWarshall(graph, 4)