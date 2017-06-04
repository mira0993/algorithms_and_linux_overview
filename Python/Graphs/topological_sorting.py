'''
* Works only when the graph is directed and acyclic
* It is a linear ordering of vertices such that for every
directed edge uv, vertex u comes before v in ordering
* It solves the scheduling task problem
'''


def topological_sorting(graph):  
    topological_sorted = []
    ready_stack = []
    count_of_dependencies = {}

    for g in graph.keys():
        count_of_dependencies[g] = 0
        for k in graph.keys():
            if k != g and g in graph[k]:
                count_of_dependencies[g] += 1
        if count_of_dependencies[g] == 0:
            ready_stack.append(g)

    while len(ready_stack) > 0:
        vertex = ready_stack.pop()
        topological_sorted.append(vertex)
        for neighbor in graph[vertex]:
            count_of_dependencies[neighbor] -= 1
            if count_of_dependencies[neighbor] == 0:
                ready_stack.append(neighbor)
    return topological_sorted

graph = {
    'A': ['C', 'D'],
    'B': ['D', 'F'],
    'C': ['D', 'E', 'H'],
    'D': ['F'],
    'E': ['G'],
    'F': ['G','H'],
    'G': ['H'],
    'H': []
}

print(topological_sorting(graph))
    