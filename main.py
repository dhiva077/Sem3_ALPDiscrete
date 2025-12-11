import sys
import os

# Cek apakah graf.py ada
if not os.path.exists('graf.py'):
    print("ERROR: File 'graf.py' tidak ditemukan!")
    print("Pastikan file 'graf.py' berada di folder yang sama.")
    sys.exit(1)

try:
    from graf import Graf
except ImportError as e:
    print(f"ERROR: Tidak dapat mengimpor dari graf.py: {e}")
    print("\nKemungkinan penyebab:")
    print("1. NetworkX tidak terinstall")
    print("2. File graf.py rusak")
    print("\nSolusi:")
    print("1. Install networkx: pip install networkx matplotlib")
    print("2. Periksa kembali file graf.py")
    sys.exit(1)

def contoh_dasar():
    """Contoh penggunaan kelas Graf."""
    print("\n" + "=" * 60)
    print("CONTOH PENGGUNAAN KELAS GRAF")
    print("=" * 60)
    
    graph = Graf(directed=False)
    
    # Menambah node
    print("\n1. Menambahkan Node:")
    for i in range(1, 6):
        result = graph.add_node(i)
        print(f"   {result}")
    
    # Menambah edge
    print("\n2. Menambahkan Edge:")
    edges = [
        (1, 2, 4.5), (1, 3, 3.2), (2, 4, 2.7),
        (3, 4, 1.8), (1, 4, 6.7), (3, 5, 2.7)
    ]
    
    for u, v, w in edges:
        result = graph.add_edge(u, v, w)
        print(f"   {result}")
    
    # Visualisasi graf
    print("\n3. Visualisasi Graf:")
    try:
        graph.visualize_graph(title="Contoh Graf", node_size=1000)
    except Exception as e:
        print(f"   Error visualisasi: {e}")
        print("   Lanjutkan tanpa visualisasi...")
    
    # Jalur terpendek
    print("\n4. Mencari Jalur Terpendek dari node 1 ke node 5:")
    path, distance = graph.shortest_path(1, 5)
    if path:
        print(f"   Jalur terpendek: {path}")
        print(f"   Jarak: {distance}")
        
        # Visualisasi jalur terpendek jika ada
        try:
            print("\n5. Visualisasi Jalur Terpendek:")
            graph.visual_shortest_path(1, 5)
        except:
            print("   (Lewati visualisasi)")
    
    # Informasi graf
    print("\n6. Informasi Graf:")
    info = graph.get_graph_info()
    for key, value in info.items():
        print(f"   {key}: {value}")
    
    # Metode tambahan
    print("\n7. Beberapa Metode Tambahan:")
    print(f"   Derajat node: {graph.get_degree()}")
    print(f"   BFS dari node 1: {graph.bfs_traversal(1)}")
    print(f"   DFS dari node 1: {graph.dfs_traversal(1)}")
    
    return graph

def run_soal_1():
    """Jalankan soal 1."""
    print("\n" + "=" * 70)
    print("SOAL 1 - GRAF TAK BERARAH, DERAJAT, DAN KONEKTIVITAS")
    print("=" * 70)
    
    try:
        # Buat graf langsung di sini (tanpa import soal1.py)
        G = Graf(directed=False)
        
        # Menambahkan node
        nodes = ['A', 'B', 'C', 'D', 'E', 'F']
        for node in nodes:
            G.add_node(node)
        
        # Menambahkan edge sesuai soal
        edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), 
                 ('C', 'E'), ('D', 'E'), ('E', 'F'), ('C', 'F')]
        
        for u, v in edges:
            G.add_edge(u, v, weight=1.0)
        
        print("\na. Visualisasi Graf:")
        try:
            G.visualize_graph(title="Soal 1 - Graf Tak Berarah", node_size=1000)
        except Exception as e:
            print(f"   (Visualisasi tidak tersedia: {e})")
        
        print("\nb. Derajat Setiap Simpul:")
        degrees = G.get_degree()
        for node, degree in sorted(degrees.items()):
            print(f"   Derajat simpul {node}: {degree}")
        
        print("\nc. Pengecekan Cycle:")
        has_cycle, cycles = G.has_cycle()
        if has_cycle:
            print(f"   Graf MEMILIKI cycle")
            if cycles:
                print(f"   Contoh cycle: {cycles[0]}")
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
        
        # BFS dan DFS
        print("\ne. Traversal:")
        print(f"   BFS dari A: {' → '.join(G.bfs_traversal('A'))}")
        print(f"   DFS dari A: {' → '.join(G.dfs_traversal('A'))}")
        
        return G
        
    except Exception as e:
        print(f"Error menjalankan soal 1: {e}")
        return None

def run_soal_3():
    """Jalankan soal 3."""
    print("\n" + "=" * 70)
    print("SOAL 3 - BFS, DFS, DAN DIJKSTRA")
    print("=" * 70)
    
    try:
        # Buat graf langsung di sini
        G = Graf(directed=False)
        
        # Menambahkan node
        nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        for node in nodes:
            G.add_node(node)
        
        # Menambahkan edge dengan bobot
        edges_with_weights = [
            ('A', 'B', 2), ('A', 'C', 5), ('B', 'D', 4),
            ('B', 'E', 6), ('C', 'F', 3), ('D', 'G', 2),
            ('E', 'F', 4), ('F', 'G', 1)
        ]
        
        for u, v, w in edges_with_weights:
            G.add_edge(u, v, weight=w)
        
        print("\na. Visualisasi Graf Berbobot:")
        try:
            G.visualize_graph(title="Soal 3 - Graf Berbobot", node_size=1000)
        except Exception as e:
            print(f"   (Visualisasi tidak tersedia: {e})")
        
        print("\nb. BFS Traversal dari Simpul A:")
        bfs_order = G.bfs_traversal('A')
        print(f"   Urutan kunjungan BFS: {' → '.join(bfs_order)}")
        
        print("\nc. DFS Traversal dari Simpul A:")
        dfs_order = G.dfs_traversal('A')
        print(f"   Urutan kunjungan DFS: {' → '.join(dfs_order)}")
        
        print("\nd. Algoritma Dijkstra dari Simpul A:")
        
        # Jarak minimum
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
            
            if path and distances[node] != float('inf'):
                print(f"      A → {node}: Jarak = {distances[node]}, Jalur = {' → '.join(path)}")
            else:
                print(f"      A → {node}: Tidak dapat dijangkau")
        
        # Jalur terpendek A ke G
        print("\n   2. Jalur terpendek dari A ke G:")
        shortest_path, distance = G.shortest_path('A', 'G')
        
        if shortest_path:
            print(f"      Jalur terpendek: {' → '.join(shortest_path)}")
            print(f"      Total jarak: {distance}")
            
            try:
                print("\n      Visualisasi jalur terpendek A → G:")
                G.visual_shortest_path('A', 'G')
            except:
                print("      (Visualisasi tidak tersedia)")
        else:
            print("      Tidak ada jalur dari A ke G")
        
        return G
        
    except Exception as e:
        print(f"Error menjalankan soal 3: {e}")
        return None

def demo_metode_tambahan():
    """Demo metode tambahan."""
    print("\n" + "=" * 70)
    print("DEMO METODE TAMBAHAN GRAF")
    print("=" * 70)
    
    try:
        # Buat graf contoh
        G = Graf(directed=False)
        
        nodes = ['X', 'Y', 'Z', 'W', 'V']
        for node in nodes:
            G.add_node(node)
        
        edges = [('X', 'Y', 2), ('X', 'Z', 3), ('Y', 'W', 4),
                 ('Z', 'W', 1), ('W', 'V', 2), ('Y', 'V', 5)]
        
        for u, v, w in edges:
            G.add_edge(u, v, w)
        
        print("\nGraf contoh dengan nodes:", nodes)
        
        print("\n1. Derajat node:")
        degrees = G.get_degree()
        for node, degree in degrees.items():
            print(f"   {node}: {degree}")
        
        print("\n2. Informasi graf:")
        info = G.get_graph_info()
        for key, value in info.items():
            print(f"   {key}: {value}")
        
        print("\n3. Bridge (jembatan):")
        try:
            bridges = G.get_bridges()
            if bridges:
                for bridge in bridges:
                    print(f"   {bridge}")
            else:
                print("   Tidak ada bridge")
        except:
            print("   (Metode tidak tersedia)")
        
        print("\n4. Clustering coefficient:")
        try:
            coeff = G.get_clustering_coefficient()
            for node, value in coeff.items():
                print(f"   {node}: {value:.3f}")
        except:
            print("   (Metode tidak tersedia)")
        
        # Coba visualisasi
        try:
            print("\n5. Visualisasi graf contoh:")
            G.visualize_graph(title="Demo Metode Tambahan", node_size=800)
        except:
            print("   (Visualisasi tidak tersedia)")
        
    except Exception as e:
        print(f"Error dalam demo: {e}")

def clear_screen():
    """Clear screen sesuai OS."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_header():
    """Tampilkan header program."""
    print("\n" + "=" * 70)
    print("IMPLEMENTASI TEORI GRAF MENGGUNAKAN PYTHON")
    print("TUGAS AKHIR SEMESTER")
    print("=" * 70)

def main():
    """Fungsi utama dengan menu berulang."""
    # Cek dependencies
    print("Mengecek dependencies...")
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
        print("✓ NetworkX dan Matplotlib terinstall!")
    except ImportError as e:
        print(f"✗ Error: {e}")
        print("\nSilakan install dependencies dengan:")
        print("pip install networkx matplotlib")
        return
    
    while True:
        show_header()
        
        print("\n" + "=" * 50)
        print("MENU UTAMA")
        print("=" * 50)
        print("1. Contoh Penggunaan Kelas Graf")
        print("2. Soal 1 - Graf Tak Berarah")
        print("3. Soal 3 - BFS, DFS, Dijkstra")
        print("4. Demo Metode Tambahan")
        print("5. Jalankan Semua (1+2+3+4)")
        print("6. Clear Screen")
        print("7. Keluar")
        print("=" * 50)
        
        try:
            pilihan = input("\nPilih menu (1-7): ").strip()
            
            if pilihan == '1':
                contoh_dasar()
                input("\nTekan Enter untuk kembali ke menu...")
                
            elif pilihan == '2':
                run_soal_1()
                input("\nTekan Enter untuk kembali ke menu...")
                
            elif pilihan == '3':
                run_soal_3()
                input("\nTekan Enter untuk kembali ke menu...")
                
            elif pilihan == '4':
                demo_metode_tambahan()
                input("\nTekan Enter untuk kembali ke menu...")
                
            elif pilihan == '5':
                print("\n" + "=" * 70)
                print("MENJALANKAN SEMUA FITUR")
                print("=" * 70)
                
                contoh_dasar()
                input("\nTekan Enter untuk lanjut ke Soal 1...")
                
                run_soal_1()
                input("\nTekan Enter untuk lanjut ke Soal 3...")
                
                run_soal_3()
                input("\nTekan Enter untuk lanjut ke Demo...")
                
                demo_metode_tambahan()
                input("\nSemua fitur selesai. Tekan Enter untuk kembali ke menu...")
                
            elif pilihan == '6':
                clear_screen()
                
            elif pilihan == '7':
                print("\n" + "=" * 70)
                print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")
                print("=" * 70)
                print("\nNama: [NAMA ANDA]")
                print("NIM: [NIM ANDA]")
                print("Mata Kuliah: Teori Graf")
                print("=" * 70)
                break
                
            else:
                print("\nPilihan tidak valid! Silakan pilih 1-7.")
                input("Tekan Enter untuk melanjutkan...")
                
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh pengguna.")
            break
        except Exception as e:
            print(f"\nError: {e}")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()