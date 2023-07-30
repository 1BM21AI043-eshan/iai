from heapq import heappop, heappush

def heuristic(node, goal):
    # Manhattan distance as the heuristic (can be modified for different problems)
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def astar(grid, start, goal):
    # Possible movements (up, down, left, right)
    movements = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    rows, cols = len(grid), len(grid[0])
    pq = [(0, start)]  # Priority queue with the starting node
    came_from = {start: None}  # Dictionary to store the path
    cost_so_far = {start: 0}  # Dictionary to store the cost to reach each node

    while pq:
        current_cost, current_node = heappop(pq)

        if current_node == goal:
            break

        for move in movements:
            next_node = current_node[0] + move[0], current_node[1] + move[1]

            if 0 <= next_node[0] < rows and 0 <= next_node[1] < cols and grid[next_node[0]][next_node[1]] != 1:
                new_cost = cost_so_far[current_node] + 1
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + heuristic(next_node, goal)
                    heappush(pq, (priority, next_node))
                    came_from[next_node] = current_node

    # Reconstruct the path from the goal to the start
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()

    return path

# Example usage:
grid = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

start = (0, 0)
goal = (3, 3)

result = astar(grid, start, goal)
print(result)
