import heapq

# Клас графа
class Graph:
    def __init__(self):
        self.edges = {}
        self.nodes = set()

    def add_node(self, value):
        self.nodes.add(value)   
        self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))    

# Створення графа
graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')

graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('D', 'E', 3)


# Алгоритм Дейкстри для знаходження найкоротших відстаней
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Використання алгоритму Дейкстри для знаходження найкоротших відстаней в графі
start_node = 'A'
distances = dijkstra(graph, start_node)
for node in distances:
    print(f'Шлях з {start_node} до {node} = {distances[node]}')