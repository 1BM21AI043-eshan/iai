from collections import deque

def bfs(graph, start_node):
    visited = set()             # Keep track of visited nodes
    queue = deque([start_node]) # Initialize the queue with the start_node
    
    while queue:
        current_node = queue.popleft()
        if current_node not in visited:
            visited.add(current_node)
            print(current_node)  # Process the current node (you can modify this part accordingly)
            
            # Enqueue all unvisited neighbors of the current node
            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    '9': ['8', '7'],
    '8': ['9', '6', '5'],
    '7': ['9', '4', '3'],
    '6': ['8'],
    '5': ['8'],
    '4': ['7'],
    '3': ['7']
}

# Start the BFS from node 'A'
bfs(graph, '9')
