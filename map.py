import csv
import networkx as nx
import matplotlib.pyplot as plt

def read_adjacencies(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        adjacency_matrix = [list(map(int, row)) for row in csv_reader]
    return adjacency_matrix

def read_positions(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        positions = {int(row[0])-1: (float(row[1]), float(row[2])) for row in csv_reader}
    return positions

def find_shortest_path(G, source, target):
    return nx.dijkstra_path(G, source, target)

def display_graph(adjacency_matrix, positions=None, source=None, target=None):
    G = nx.Graph()
    for i, row in enumerate(adjacency_matrix):
        for j in row:
            print(f"Adding edge {i} -> {j}")
            G.add_edge(i, j)

    if positions is None:
        positions = nx.spring_layout(G)

    plt.figure(dpi=320)
    nx.draw_networkx_edges(G, positions, edge_color='black', width=0.2)

    if source is not None and target is not None:
        print("Finding shortest path...")
        shortest_path = find_shortest_path(G, source, target)
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, positions, edgelist=path_edges, edge_color='red', width=0.5)

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    plt.show()

def main():
    adjacency_matrix = read_adjacencies('adjacencies.csv')
    province_positions = read_positions('positions.csv')

    print("===== Pathmaker =====")
    start = int(input("Enter the source province: ")) - 1
    end = int(input("Enter the target province: ")) - 1

    display_graph(adjacency_matrix, positions=province_positions, source=start, target=end)

if __name__ == '__main__':
    main()
