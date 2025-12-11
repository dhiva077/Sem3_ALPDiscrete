# Sem3_ALPDiscrete

## Overview
Projek ini merupakan bentuk implementasi teori graf dalam Python. Beberapa operasi dari teori tersebut telah diubah menjadi *methods* yang siapa digunakan untuk melakukan beberapa operasi dalam teori graf. Semua *method* ini digabung dalam sebuah class `Graf` yang pada dasarnya menggunakan library lain, yaitu *etworkX*, *matplotlib.pyplot*, dan *deque*.

## Class Methods

### `__init__(directed=False)`
Sebagai inisialisasi untuk membuat objek graf. Parameter directed menentukan apakah graf berarah atau tidak.
```
Graf tak Berarah:
graph = Graf()

Graf Berarah:
graph_directed = Graf(directed=True)
```

### `add_node(node)`
Digunakan untuk menambah sebuah node (titik/simpul) dalam graf.
```
G = Graf()
G.add_node('A')
G.add_node('B')
G.add_node('C')
```

### `add_edge(u, v, weight=1.0)`
Menambahkan edge (sisi) antara dua node dengan bobot opsional.
```
G.add_edge('A', 'B', weight=4.5)
G.add_edge('B', 'C', weight=3.2)
```

### `visualize_graph(title="Visualisasi Graf", node_size=800, with_labels=True)`
Menampilkan visualisasi graf menggunakan matplotlib.
```
graph.visualize_graph(title="Graf Contoh", node_size=1000)
```

### `shortest_path(start, end)`
Mencari jalur terpendek antara dua node menggunakan algoritma Dijkstra.
```
path, distance = graph.shortest_path('A', 'G')
print(f"Jalur: {path}, Jarak: {distance}")
```

### `visual_shortest_path(start, end)`
Menampilkan visualisasi graf dengan highlight pada jalur terpendek.
```
graph.visual_shortest_path('A', 'G')
```

### `get_degree(node=None)`
Mendapatkan derajat node. Jika node=None, kembalikan semua derajat.
```
# Derajat semua node
degrees = graph.get_degree()
print(degrees)  # {'A': 2, 'B': 3, 'C': 1}

# Derajat node spesifik
degree_A = graph.get_degree('A')
print(degree_A)  # {'A': 2}
```

### `is_connected()`
Mengecek apakah graf terhubung (connected).
```
if graph.is_connected():
    print("Graf terhubung")
else:
    print("Graf tidak terhubung")
```

### `has_cycle()`
Mengecek apakah graf memiliki cycle.
```
has_cycle, cycles = graph.has_cycle()
if has_cycle:
    print(f"Graf memiliki cycle: {cycles}")
else:
    print("Graf tidak memiliki cycle")
```

### `bfs_traversal(start)`
Traversal Breadth-First Search (BFS) dari node awal.
```
bfs_result = graph.bfs_traversal('A')
print(f"BFS: {' → '.join(bfs_result)}")
```

### `dfs_traversal(start)`
Traversal Depth-First Search (DFS) dari node awal.
```
dfs_result = graph.dfs_traversal('A')
print(f"DFS: {' → '.join(dfs_result)}")
```

### `get_all_shortest_paths_dijkstra(start)`
Mencari semua jarak terpendek dari node awal ke semua node lain.
```
distances, paths = graph.get_all_shortest_paths_dijkstra('A')
for node, dist in distances.items():
    print(f"A → {node}: {dist}")
```

### `get_graph_info()`
Mendapatkan informasi lengkap graf dalam bentuk dictionary.
```
info = graph.get_graph_info()
for key, value in info.items():
    print(f"{key}: {value}")
```

### `remove_node(node)`
Menghapus node dari graf.
```
result = graph.remove_node('A')
print(result)  # "Node A berhasil dihapus"
```

### `remove_edge(u, v)`
Menghapus edge antara dua node.
```
result = graph.remove_edge('A', 'B')
print(result)  # "Edge (A, B) berhasil dihapus"
```

### Metode Tambahan Lainnya:
get_diameter() - Mendapatkan diameter graf
get_eccentricity(node) - Mendapatkan eksentrisitas node
get_radius() - Mendapatkan radius graf
get_center() - Mendapatkan center graf
is_tree() - Mengecek apakah graf adalah pohon
get_adjacency_matrix() - Matriks adjacency
get_laplacian_matrix() - Matriks Laplacian
get_clustering_coefficient(node=None) - Clustering coefficient
get_bridges() - Mendapatkan semua bridge edges
get_articulation_points() - Mendapatkan articulation points

## Penyelesaian Soal
### Soal 1: Graf Tak Berarah, Derajat, dan Konektivitas
V = {A, B, C, D, E, F}
E = {(A,B),(A,C),(B,D),(C,E),(D,E),(E,F),(C,F)}

Hasil:

Derajat: A:2, B:2, C:3, D:2, E:3, F:2
Cycle: Ya, contoh: A-C-F-E-C
Konektivitas: Graf terhubung

### Soal 3: BFS, DFS, dan Dijkstra
V = {A, B, C, D, E, F, G}
E = {(A,B,2),(A,C,5),(B,D,4),(B,E,6),(C,F,3),(D,G,2),(E,F,4),(F,G,1)}

Hasil:

BFS dari A: A → B → C → D → E → F → G
DFS dari A: A → B → D → G → E → F → C
Dijkstra dari A:

A→G: Jalur A-B-D-G, Jarak 8

## Cara penggunaan
## 1. Instalasi Dependencies
### Install dependencies
pip install networkx matplotlib numpy

## 2. Jalan Program
### Metode 1: Jalankan langsung
python main.py

## Metode 2: Dengan script (macOS/Linux)
chmod +x run_program.sh
./run_program.sh

# Metode 3: Dengan script (Windows)
run.bat

### 3. Contoh Penggunaan dalam Code
from graf import Graf

### Buat graf
g = Graf()

### Tambah node dan edge
g.add_node('A')
g.add_node('B')
g.add_edge('A', 'B', weight=5)

### Cari jalur terpendek
path, dist = g.shortest_path('A', 'B')
print(f"Jalur: {path}, Jarak: {dist}")

### Visualisasi
g.visualize_graph()

## Menu Program Utama
Program utama (main.py) menyediakan menu interaktif dengan 7 pilihan:

Contoh Penggunaan Kelas Graf - Demonstrasi dasar
Soal 1 - Graf tak berarah, derajat, dan konektivitas
Soal 3 - BFS, DFS, dan algoritma Dijkstra
Demo Metode Tambahan - Berbagai metode analisis graf
Jalankan Semua - Menjalankan semua fitur sekaligus
Clear Screen - Membersihkan layar
Keluar - Keluar dari program

## Installation
## Persyaratan Sistem
Python 3.6 atau lebih tinggi
pip (Python package installer)

## Anggota Kelompok
1. Dhiva Kesuma Pertiwi (0806022410025)
2. Arsya Aulia Amira (0806022410012)
3. St Mutmainnah (0806022410027)