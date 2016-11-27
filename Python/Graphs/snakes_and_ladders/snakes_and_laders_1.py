# https://www.topcoder.com/community/data-science/data-science-tutorials/introduction-to-graphs-and-their-data-structures-section-2/#breadth
# http://theoryofprogramming.com/2014/12/25/snakes-and-ladders-game-code/


# We use breadth first search (BST) because it has the extremely useful property that if all of the edges in a graph are unweighted (or the same weight) then the first time a node is visited is the shortest path to that node from the source node.

# Steps to solve the problem:

# 1. We add the connections between each block in base of the dice: For example, from block 1 I can reach block 2,3,4,5,6 and 7.
# 2. We change the value of the block when we have a ladder or snake. For example, if we have a ladder in block 6 that take us to  block 34, then all the blocks 6 will be changed to 34.
# 3. We start the BST in block 1 until we get to block 100.
#    -> In the visited list, we sve which is the node we visited before (parent) so we can then calculate the path we followed as well as the shorter number of steps we can take.

def print_graph(g):
    '''
    Print the graph
    '''

    for i in range(1, 101):
        print("%d => %s" % (i,g[i]))

def create_generic_graph():
    '''
    Create the generic board graph base on the blocks you can move
    when you get a number in the dice (from 1 to 6).

    graph = {1: [2,3,4,5,6,7], 2: [3,4,5,6,7,8], ....}
    '''

    graph = {}
    for i in range(1, 101):
        graph[i] = [i+j for j in range(1,7) if i+j <= 100]
    return graph


def add_ladder_or_snake(graph, start, end):
    '''
    Substitutes the original number we have in the graph,
    for the number that we get after going up to the ladder or down through
    the snake.
    '''

    for k in range(start - 6, start):
        if k > 0 and start in graph[k]:
            graph[k][graph[k].index(start)] = end

def bfs(graph, start):
    '''
    BFS - We use a queue to visit all the nodes.
    We save track of the visited nodes.
    '''

    queue = [start]
    visited = {start:None}
    found = False

    while len(queue) > 0:
        node = queue.pop(0)
        if node == 100:
            found = True
            break
        for next_node in graph[node]:
            if next_node not in visited:
                visited[next_node] = node
                queue.append(next_node)
    if found:
        return get_path_and_steps(visited, 100)
    return -1

def get_path_and_steps(visited, end):
    '''
    Calculate the path by going back from
    block 100 to the parent nodes saved in the visited list.
    '''
    path = []
    steps = 0

    node = end
    while node != 1:
        if node in visited:
            path.append(node)
            steps+=1
        node = visited[node]
    return steps

# Test cases
N = int(input())

for n in range(N):
    # Create board graph
    graph = create_generic_graph()
    # Add Ladders
    for m in range(int(input())):
        start, end = map(int,input().strip().split())
        add_ladder_or_snake(graph, start, end)
    # Add snakes
    for m in range(int(input())):
        start, end = map(int,input().strip().split())
        add_ladder_or_snake(graph, start, end)
    # Get shortest path
    print(bfs(graph, 1))
