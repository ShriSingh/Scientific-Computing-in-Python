copper = {
    'species': 'guinea pig',
    'age': 2
}

copper['food'] = 'hay' # Adding a new key-value pair
copper['species'] = 'Cavia porcellus' # Modifying an existing key-value pair
del copper['age'] # Deleting a key-value pair

# {key: val for key in dict} --> Dicionary comprehension

# Learning algorithm design by building a shortest path algorithm

def shortest_path(graph, start, target = ''):
    """
    Creating a shortest path algorithm to learn Algorithm Design
    : param graph: The graph to traverse
    : param start: The starting node
    : param target: The target node (optional; if not provided, all nodes are considered)
    """
    unvisited = list(graph) # List of all nodes(keys) in the graph dictionary
    # Dictionary comprehension to initialize the distances to all nodes as infinity except the start node
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph} # Dictionary to store the shortest path to each node
    paths[start].append(start) # Add the start node to the path
    
    # While loop to traverse the graph nodes
    while unvisited:
        current = min(unvisited, key=distances.get) # Gets the node with the smallest distance from the start
        for node, distance in graph[current]:
            # Checking if the distance of the neighbor node(2nd item in the tuple) + the distance of current node < distance of the neighbor node
            if distance + distances[current] < distances[node]:
                # Update the distance of the neighbor node
                distances[node] = distance + distances[current]
                # Checking if the path to the neighbor node is empty or if the last node in the path is the current node
                if paths[node] and paths[node][-1] == node:
                    # Assigning a copy of paths[current] to neighbor node path
                    paths[node] = paths[current][:] # Preventing both paths from modified when appending the neighbor node
                else:
                    # Adding the current node path to the neighbor node path
                    paths[node].extend(paths[current])
                # Adding the neighbor node to its path
                paths[node].append(node)
        # Remove the current node from the unvisited list
        unvisited.remove(current)
    
    # Print the shortest path to the target node
    targets_to_print = [target] if target else graph
    # Loop through the target nodes
    for node in targets_to_print:
        # Skip the start node as the distance to it would be 0
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths

if __name__ == '__main__':
    my_graph = {
        'A': [('B', 5), ('C', 3), ('E', 11)],
        'B': [('A', 5), ('C', 1), ('F', 2)],
        'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
        'D': [('C',1 ), ('E', 9), ('F', 3)],
        'E': [('A', 11), ('C', 5), ('D', 9)],
        'F': [('B', 2), ('D', 3)]
    }
    
    print(shortest_path(my_graph, 'A', 'F'))
