from graf import Graf

def soal_1():
    """
    Menyelesaikan Soal 1:
    Graf Tak Berarah, Derajat, dan Konektivitas
    """
    print("=" * 60)
    print("SOAL 1 - GRAF TAK BERARAH, DERAJAT, DAN KONEKTIVITAS")
    print("=" * 60)
    
    # Membuat objek graf
    G = Graf(directed=False)
    
    # Menambahkan node
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    for node in nodes:
        G.add_node(node)
    
    # Menambahkan edge sesuai soal
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), 
             ('C', 'E'), ('D', 'E'), ('E', 'F'), ('C', 'F')]
    
    for u, v in edges:
        G.add_edge(u, v, weight=1.0)  # Bobot default 1 untuk graf tak berbobot
    
    print("\na. Visualisasi Graf:")
    G.visualize_graph(title="Soal 1 - Graf Tak Berarah", node_size=1000)
    
    print("\nb. Derajat Setiap Simpul:")
    degrees = G.get_degree()
    for node, degree in sorted(degrees.items()):
        print(f"   Derajat simpul {node}: {degree}")
    
    print("\nc. Pengecekan Cycle:")
    has_cycle, cycles = G.has_cycle()
    if has_cycle:
        print(f"   Graf MEMILIKI cycle")
        if cycles:
            print(f"   Cycle yang ditemukan: {cycles}")
    else:
        print("   Graf TIDAK memiliki cycle")
    
    print("\nd. Konektivitas Graf:")
    is_conn = G.is_connected()
    if is_conn:
        print("   Graf TERHUBUNG (connected)")
        print("   Alasan: Semua node dapat dijangkau dari node manapun")
    else:
        print("   Graf TIDAK terhubung")
        print("   Alasan: Ada node yang tidak dapat dijangkau dari node tertentu")
    
    # Menampilkan informasi tambahan
    print("\n" + "=" * 60)
    print("INFORMASI TAMBAHAN GRAF SOAL 1:")
    print("=" * 60)
    
    info = G.get_graph_info()
    for key, value in info.items():
        print(f"{key:20}: {value}")
    
    # Menampilkan BFS dan DFS
    print("\nBFS dari A:")
    bfs_result = G.bfs_traversal('A')
    print(f"   Urutan: {' → '.join(bfs_result)}")
    
    print("\nDFS dari A:")
    dfs_result = G.dfs_traversal('A')
    print(f"   Urutan: {' → '.join(dfs_result)}")
    
    return G

if __name__ == "__main__":
    soal_1()