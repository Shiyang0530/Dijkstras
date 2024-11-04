import heapq

graph_data = {
    'A': [('B', 5), ('C', 4), ('D', 6)],
    'B': [('A', 5), ('E', 8)],
    'C': [('A', 4), ('G', 5)],
    'D': [('A', 6), ('F', 2)],
    'E': [('B', 8), ('G', 3)],
    'F': [('D', 2), ('G', 2)],
    'G': [('C', 5), ('E', 3), ('H', 1), ('F', 2)],
    'H': [('G', 1), ('I', 4)],
    'I': [('H', 4), ('J', 1)],
    'J': [('I', 1)]
}


def dijkstra(graph, start, target):
    # Priority queue to store (distance, vertex)
    queue = [(0, start)]
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    previous_nodes = {vertex: None for vertex in graph}

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        # Stop if the target is reached
        if current_vertex == target:
            break

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Only consider this path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(queue, (distance, neighbor))

    # Construct the shortest path
    path, current = [], target
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return distances[target], path


shortest_distance, shortest_path = dijkstra(graph_data, 'A', 'J')
var = shortest_distance, shortest_path
print(shortest_path)
print(shortest_distance)