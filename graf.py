import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
import heapq

class Graf:
    def __init__(self, directed=False):
        """
        Inisialisasi objek graf.
        
        Parameters:
        - directed: Boolean, True untuk graf berarah, False untuk tak berarah
        """
        self.graph = nx.Graph() if not directed else nx.DiGraph()
        self.node_positions = {}
        
    def add_node(self, node):
        """
        Menambahkan node ke dalam graf.
        
        Parameters:
        - node: Node yang akan ditambahkan
        """
        self.graph.add_node(node)
        return f"Node {node} berhasil ditambahkan"
    
    def add_edge(self, u, v, weight=1.0):
        """
        Menambahkan edge antara dua node.
        
        Parameters:
        - u: Node pertama
        - v: Node kedua
        - weight: Bobot edge (default: 1.0)
        """
        self.graph.add_edge(u, v, weight=weight)
        return f"Edge ({u}, {v}) dengan bobot {weight} berhasil ditambahkan"
    
    def remove_node(self, node):
        """
        Menghapus node dari graf.
        
        Parameters:
        - node: Node yang akan dihapus
        """
        if node in self.graph:
            self.graph.remove_node(node)
            return f"Node {node} berhasil dihapus"
        return f"Node {node} tidak ditemukan"
    
    def remove_edge(self, u, v):
        """
        Menghapus edge antara dua node.
        
        Parameters:
        - u: Node pertama
        - v: Node kedua
        """
        if self.graph.has_edge(u, v):
            self.graph.remove_edge(u, v)
            return f"Edge ({u}, {v}) berhasil dihapus"
        return f"Edge ({u}, {v}) tidak ditemukan"
    
    def visualize_graph(self, title="Visualisasi Graf", node_size=800, with_labels=True):
        """
        Menampilkan visualisasi graf.
        
        Parameters:
        - title: Judul visualisasi
        - node_size: Ukuran node
        - with_labels: Tampilkan label node
        """
        plt.figure(figsize=(10, 8))
        
        # Gunasi layout yang konsisten untuk visualisasi
        if not self.node_positions:
            self.node_positions = nx.spring_layout(self.graph, seed=42)
        
        pos = self.node_positions
        
        # Gambar graf
        nx.draw(self.graph, pos, with_labels=with_labels, node_size=node_size, 
                node_color='lightblue', font_size=10, font_weight='bold')
        
        # Tambahkan label bobot untuk edge
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        if edge_labels:
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        
        plt.title(title)
        plt.axis('off')
        plt.show()
        
    def shortest_path(self, start, end):
        """
        Mencari jalur terpendek antara dua node menggunakan Dijkstra.
        
        Parameters:
        - start: Node awal
        - end: Node tujuan
        
        Returns:
        - List jalur terpendek
        """
        try:
            path = nx.dijkstra_path(self.graph, start, end)
            distance = nx.dijkstra_path_length(self.graph, start, end)
            return path, distance
        except nx.NetworkXNoPath:
            return None, float('inf')
        except nx.NodeNotFound:
            return None, float('inf')
    
    def visual_shortest_path(self, start, end):
        """
        Menampilkan visualisasi graf dengan jalur terpendek.
        
        Parameters:
        - start: Node awal
        - end: Node tujuan
        """
        path, distance = self.shortest_path(start, end)
        
        if path is None:
            print(f"Tidak ada jalur dari {start} ke {end}")
            return
        
        plt.figure(figsize=(10, 8))
        
        if not self.node_positions:
            self.node_positions = nx.spring_layout(self.graph, seed=42)
        
        pos = self.node_positions
        
        # Gambar seluruh graf
        nx.draw(self.graph, pos, with_labels=True, node_size=800,
                node_color='lightblue', font_size=10, font_weight='bold')
        
        # Gambar edge pada jalur terpendek dengan warna merah
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(self.graph, pos, edgelist=path_edges, 
                              width=3, edge_color='red')
        
        # Highlight node pada jalur terpendek
        nx.draw_networkx_nodes(self.graph, pos, nodelist=path,
                              node_color='red', node_size=800)
        
        # Tambahkan label bobot
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        if edge_labels:
            nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        
        plt.title(f"Jalur Terpendek dari {start} ke {end}\nJalur: {path}\nJarak: {distance}")
        plt.axis('off')
        plt.show()
    
    # =========== METODE TAMBAHAN ===========
    
    def get_degree(self, node=None):
        """
        Mendapatkan derajat node.
        
        Parameters:
        - node: Node spesifik (jika None, kembalikan semua derajat)
        
        Returns:
        - Dictionary derajat node
        """
        if node:
            if node in self.graph:
                return {node: self.graph.degree(node)}
            return {node: 0}
        return dict(self.graph.degree())
    
    def is_connected(self):
        """
        Mengecek apakah graf terhubung.
        
        Returns:
        - Boolean True jika graf terhubung
        """
        return nx.is_connected(self.graph) if not self.graph.is_directed() else \
               nx.is_weakly_connected(self.graph)
    
    def has_cycle(self):
        """
        Mengecek apakah graf memiliki cycle.
        
        Returns:
        - Boolean True jika ada cycle
        """
        try:
            cycles = list(nx.find_cycle(self.graph))
            return True, cycles
        except nx.NetworkXNoCycle:
            return False, []
    
    def bfs_traversal(self, start):
        """
        Melakukan traversal Breadth-First Search (BFS).
        
        Parameters:
        - start: Node awal
        
        Returns:
        - List urutan kunjungan BFS
        """
        if start not in self.graph:
            return []
        
        visited = []
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                neighbors = sorted(list(self.graph.neighbors(node)))
                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)
        
        return visited
    
    def dfs_traversal(self, start):
        """
        Melakukan traversal Depth-First Search (DFS) rekursif.
        
        Parameters:
        - start: Node awal
        
        Returns:
        - List urutan kunjungan DFS
        """
        if start not in self.graph:
            return []
        
        visited = []
        
        def dfs_recursive(node):
            visited.append(node)
            neighbors = sorted(list(self.graph.neighbors(node)))
            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs_recursive(neighbor)
        
        dfs_recursive(start)
        return visited
    
    def get_all_shortest_paths_dijkstra(self, start):
        """
        Mencari semua jalur terpendek dari node awal ke semua node lainnya.
        
        Parameters:
        - start: Node awal
        
        Returns:
        - Dictionary jarak minimum ke semua node
        """
        distances = {node: float('inf') for node in self.graph.nodes()}
        distances[start] = 0
        
        # Priority queue: (distance, node)
        pq = [(0, start)]
        previous_nodes = {node: None for node in self.graph.nodes()}
        
        while pq:
            current_distance, current_node = heapq.heappop(pq)
            
            if current_distance > distances[current_node]:
                continue
            
            for neighbor in self.graph.neighbors(current_node):
                weight = self.graph[current_node][neighbor].get('weight', 1)
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances, previous_nodes
    
    def get_diameter(self):
        """
        Menghitung diameter graf (panjang jalur terpanjang terpendek).
        
        Returns:
        - Diameter graf
        """
        if not self.is_connected():
            return float('inf')
        return nx.diameter(self.graph)
    
    def get_eccentricity(self, node):
        """
        Menghitung eksentrisitas node.
        
        Parameters:
        - node: Node yang akan dihitung eksentrisitasnya
        
        Returns:
        - Eksentrisitas node
        """
        if node not in self.graph:
            return None
        return nx.eccentricity(self.graph, node)
    
    def get_radius(self):
        """
        Menghitung radius graf.
        
        Returns:
        - Radius graf
        """
        if not self.is_connected():
            return float('inf')
        return nx.radius(self.graph)
    
    def get_center(self):
        """
        Mendapatkan center dari graf.
        
        Returns:
        - List node yang merupakan center
        """
        if not self.is_connected():
            return []
        return nx.center(self.graph)
    
    def is_tree(self):
        """
        Mengecek apakah graf merupakan pohon.
        
        Returns:
        - Boolean True jika graf adalah pohon
        """
        return nx.is_tree(self.graph)
    
    def get_adjacency_matrix(self):
        """
        Mendapatkan matriks adjacency.
        
        Returns:
        - Matriks adjacency sebagai list of lists
        """
        return nx.adjacency_matrix(self.graph).todense()
    
    def get_laplacian_matrix(self):
        """
        Mendapatkan matriks Laplacian.
        
        Returns:
        - Matriks Laplacian sebagai list of lists
        """
        return nx.laplacian_matrix(self.graph).todense()
    
    def get_clustering_coefficient(self, node=None):
        """
        Menghitung clustering coefficient.
        
        Parameters:
        - node: Node spesifik (jika None, kembalikan semua)
        
        Returns:
        - Clustering coefficient
        """
        if node:
            return nx.clustering(self.graph, node)
        return nx.clustering(self.graph)
    
    def get_average_clustering(self):
        """
        Menghitung rata-rata clustering coefficient.
        
        Returns:
        - Rata-rata clustering coefficient
        """
        return nx.average_clustering(self.graph)
    
    def get_bridges(self):
        """
        Mendapatkan semua bridge (edge) dalam graf.
        
        Returns:
        - List bridge edges
        """
        return list(nx.bridges(self.graph))
    
    def get_articulation_points(self):
        """
        Mendapatkan semua articulation points (cut vertices).
        
        Returns:
        - List articulation points
        """
        return list(nx.articulation_points(self.graph))
    
    def get_graph_info(self):
        """
        Mendapatkan informasi lengkap graf.
        
        Returns:
        - Dictionary berisi informasi graf
        """
        info = {
            "Jumlah Node": self.graph.number_of_nodes(),
            "Jumlah Edge": self.graph.number_of_edges(),
            "Tipe Graf": "Berarah" if self.graph.is_directed() else "Tak Berarah",
            "Terhubung": self.is_connected(),
            "Memiliki Cycle": self.has_cycle()[0],
            "Adalah Tree": self.is_tree(),
            "Diameter": self.get_diameter() if self.is_connected() else "Tidak Terhubung",
            "Radius": self.get_radius() if self.is_connected() else "Tidak Terhubung",
            "Center Nodes": self.get_center() if self.is_connected() else "Tidak Terhubung"
        }
        return info