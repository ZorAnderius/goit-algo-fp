import heapq

from graph_interface import *
from graph_data import graph

def dijkstra(graph: nx.Graph, start: str) -> dict:
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        current_dist, current_node = heapq.heappop(queue)
        
        if current_dist > distances[current_node]:
            continue
            
        for neighbor, node in graph[current_node].items():
            new_dist = current_dist + node['weight']
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))
                
    return distances

def show_shortest_path_way(graph: nx.Graph) -> None:
    all_pairs_shortest_paths = {node: dijkstra(graph, node) for node in graph.nodes()}
    for node, neighbors in all_pairs_shortest_paths.items():
        print(f"Найкоротші шляхи від {node}:")
        for neighbor, weight in neighbors.items():
            print(f"До {neighbor}: {weight}")
        print('_' * 64 + '\n')

def task3() -> None:
    new_graph = create_graph(graph, is_loaded=True)
    show_graph(new_graph)
    show_shortest_path_way(new_graph)
    
    shortest_path_lengths = nx.single_source_dijkstra_path_length(new_graph, source='A')
    print('\nПеревірка правильності розрахунку розробленого та бібліотечного алгоритмів Дейкстри \n')
    
    print('\nРозроблений алгоритм Дейкстри:')
    print(sorted(dijkstra(new_graph, 'A').items(),  key=lambda item: item[1]))
    
    print('\nБібліотечний алгоритм Дейкстри:')
    print(shortest_path_lengths) 


if __name__ == "__main__":
    task3()
