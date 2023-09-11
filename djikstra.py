import heapq

def dijkstra(graph, start, end):
    # Initialize distances to all nodes as infinity, except for the start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to store nodes with their current distances
    priority_queue = [(0, start)]
    
    # Dictionary to store the previous node in the shortest path
    previous = {}
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we've reached the end node, reconstruct and return the path
        if current_node == end:
            path = []
            total_cost = 0
            while current_node:
                path.append(current_node)
                total_cost += distances[current_node]
                current_node = previous.get(current_node)
            return total_cost, list(reversed(path))
        
        # If we've already processed this node, skip it
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If this path is shorter than the currently known distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # If no path from start to end is found, return None
    return None

# Example usage:
if __name__ == "__main__":
    # Define the graph as an adjacency dictionary

    graph = {
            'A': {'B': 1, 'C': 3, 'D': 5},
            'B': {'A': 1, 'E': 7, 'F': 4},
            'C': {'A': 3, 'F': 1},
            'D': {'A': 5, 'G': 2},
            'E': {'B': 7, 'G': 1,'H': 6},
            'F': {'B': 4, 'C': 1, 'G': 2},
            'G': {'D': 2, 'E': 1, 'F': 2, 'J': 4, 'L': 1},
            'H': {'E': 6, 'I': 2, 'M': 4},
            'I': {'H': 2, 'J': 1, 'K': 1, 'M': 7},
            'J': {'F': 6, 'G': 4, 'I': 1},
            'K': {'I': 1, 'L': 4},
            'L': {'G': 1, 'M': 3},
            'M': {'H': 4, 'I': 7, 'L': 3}
    }
    
    start_node = 'A'
    end_node = 'D'
    
    result = dijkstra(graph, start_node, end_node)
    
    if result:
        total_cost, shortest_path = result
        print(f'Total cost from {start_node} to {end_node}: {total_cost}')
        print(f'Shortest path: {" -> ".join(shortest_path)}')
    else:
        print(f'No path from {start_node} to {end_node} found.')
