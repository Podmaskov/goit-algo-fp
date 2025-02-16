import heapq

def dijkstra(graph, start):

    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue  

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Use

graph = {
    'S': {'A': 10, 'C': 3},
    'A': {'B': 2, 'C': 1},
    'B': {'D': 7},
    'C': {'A': 4, 'B': 8, 'D': 2},
    'D': {'B': 3, 'S': 5}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

print(f"The shortest paths from the top {start_node}:")
for vertex, distance in shortest_paths.items():
    print(f"to {vertex}: {distance}")