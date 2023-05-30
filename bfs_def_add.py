def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node, q):
    visited.add(node)
    q.append(node)
    while q:
        s = q.pop(0)
        print(s, end=" ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                q.append(neighbour)

# def goal_state(goal, visited):
#     for i in visited:
#         print(i, end=" ")
#         if i == goal:
#             break


def main():
    visited1 = set()
    visited2 = set()

    queue = []
    n = int(input("Enter number of nodes: "))
    graph = dict()

    for i in range(1, n+1):
        edges = int(input("Enter number of edges for node {}: ".format(i)))
        graph[i] = list()
        for j in range(1, edges+1):
            node = int(input("Enter edge {} for node {}: ".format(j,i)))
            graph[i].append(node)

    print("The following is DFS: ")
    dfs(visited1, graph, 1)

    print()

    print("The following is BFS: ")
    bfs(visited2, graph, 1, queue)

    # goal = int(input("\nEnter the goal state: "))

    # print("\nGoal state by BFS: ")
    # goal_state(goal, visited2)

    # print("\nGoal state by DFS: ")
    # goal_state(goal, visited1)

#main function 
if __name__ == "__main__":
    main()