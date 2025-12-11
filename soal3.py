from graf import Graf

def soal_3():
    """
    Menyelesaikan Soal 3:
    BFS, DFS, dan Dijkstra
    """
    print("=" * 60)
    print("SOAL 3 - BFS, DFS, DAN DIJKSTRA")
    print("=" * 60)
    
    # Membuat objek graf
    G = Graf(directed=False)
    
    # Menambahkan node
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    for node in nodes:
        G.add_node(node)
    
    # Menambahkan edge dengan bobot sesuai soal
    edges_with_weights = [
        ('A', 'B', 2), ('A', 'C', 5), ('B', 'D', 4),
        ('B', 'E', 6), ('C', 'F', 3), ('D', 'G', 2),
        ('E', 'F', 4), ('F', 'G', 1)
    ]
    
    for u, v, w in edges_with_weights:
        G.add_edge(u, v, weight=w)
    
    print("\na. Visualisasi Graf Berbobot:")
    G.visualize_graph(title="Soal 3 - Graf Berbobot", node_size=1000)
    
    print("\nb. BFS Traversal dari Simpul A:")
    bfs_order = G.bfs_traversal('A')
    print(f"   Urutan kunjungan BFS: {' → '.join(bfs_order)}")
    
    print("\nc. DFS Traversal dari Simpul A (rekursif, urutan alfabet):")
    dfs_order = G.dfs_traversal('A')
    print(f"   Urutan kunjungan DFS: {' → '.join(dfs_order)}")
    
    print("\nd. Algoritma Dijkstra dari Simpul A:")
    
    # 1. Jarak minimum dari A ke seluruh simpul
    print("\n   1. Jarak minimum dari A ke seluruh simpul:")
    distances, previous_nodes = G.get_all_shortest_paths_dijkstra('A')
    
    for node in sorted(nodes):
        if node == 'A':
            continue
        path = []
        current = node
        while current is not None:
            path.insert(0, current)
            current = previous_nodes[current]
        
        if path:
            print(f"      A → {node}: Jarak = {distances[node]:.1f}, Jalur = {' → '.join(path)}")
        else:
            print(f"      A → {node}: Tidak dapat dijangkau")
    
    # 2. Jalur terpendek dari A ke G
    print("\n   2. Jalur terpendek dari A ke G:")
    shortest_path, distance = G.shortest_path('A', 'G')
    
    if shortest_path:
        print(f"      Jalur terpendek: {' → '.join(shortest_path)}")
        print(f"      Total jarak: {distance}")
        
        # Visualisasi jalur terpendek
        print("\n      Visualisasi jalur terpendek A → G:")
        G.visual_shortest_path('A', 'G')
    else:
        print("      Tidak ada jalur dari A ke G")
    
    return G

if __name__ == "__main__":
    soal_3()