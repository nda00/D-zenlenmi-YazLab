# ==============================
# GEREKLİ KÜTÜPHANELER
# ==============================

import networkx as nx
import matplotlib.pyplot as plt


# ==============================
# GRAF OLUŞTUR
# ==============================

G = nx.Graph()
# Sosyal ağı temsil eden boş grafik


# ==============================
# KULLANICI (DÜĞÜM) EKLE
# ==============================

def kullanici_ekle(id, isim, aktiflik):
    # Graf içine kullanıcı ekler
    G.add_node(id, isim=isim, aktiflik=aktiflik)


# ==============================
# BAĞLANTI (KENAR) EKLE
# ==============================

def baglanti_ekle(a, b):
    # Aktiflik farkına göre ağırlık hesapla
    agirlik = abs(G.nodes[a]["aktiflik"] - G.nodes[b]["aktiflik"]) + 1
    G.add_edge(a, b, weight=agirlik)


# ==============================
# ÖRNEK KULLANICILAR
# ==============================

kullanici_ekle("1", "Ali", 0.9)
kullanici_ekle("2", "Ayşe", 0.7)
kullanici_ekle("3", "Mehmet", 0.5)
kullanici_ekle("4", "Zeynep", 0.6)


# ==============================
# ÖRNEK BAĞLANTILAR
# ==============================

baglanti_ekle("1", "2")
baglanti_ekle("2", "3")
baglanti_ekle("3", "4")
baglanti_ekle("1", "4")


# ==============================
# BFS (GENİŞLİK ÖNCELİKLİ ARAMA)
# ==============================

def bfs(baslangic):
    ziyaret = []
    kuyruk = [baslangic]

    while kuyruk:
        dugum = kuyruk.pop(0)
        if dugum not in ziyaret:
            ziyaret.append(dugum)
            kuyruk.extend(list(G.neighbors(dugum)))

    return ziyaret


# ==============================
# DFS (DERİNLİK ÖNCELİKLİ ARAMA)
# ==============================

def dfs(baslangic):
    ziyaret = []
    stack = [baslangic]

    while stack:
        dugum = stack.pop()
        if dugum not in ziyaret:
            ziyaret.append(dugum)
            stack.extend(list(G.neighbors(dugum)))

    return ziyaret


# ==============================
# DIJKSTRA (EN KISA YOL)
# ==============================

def dijkstra(a, b):
    return nx.dijkstra_path(G, a, b, weight="weight")


# ==============================
# A* (A-STAR) ALGORİTMASI
# ==============================

def a_star(a, b):
    return nx.astar_path(
        G,
        a,
        b,
        heuristic=lambda x, y: 1,  # basit heuristic
        weight="weight"
    )


# ==============================
# MERKEZİLİK (DEGREE CENTRALITY)
# ==============================

def merkezilik():
    derece = dict(G.degree())
    sirali = sorted(derece.items(), key=lambda x: x[1], reverse=True)
    return sirali


# ==============================
# WELSH–POWELL RENKLENDİRME
# ==============================

def renklendir():
    return nx.coloring.greedy_color(G, strategy="largest_first")


# ==============================
# GRAFI ÇİZ
# ==============================

def grafigi_ciz():
    pos = nx.spring_layout(G)

    renkler = renklendir()
    node_colors = [renkler[node] for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000)

    agirliklar = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=agirliklar)

    plt.show()


# ==============================
# PROGRAM ÇALIŞTIRMA
# ==============================

grafigi_ciz()

print("BFS:", bfs("1"))
print("DFS:", dfs("1"))
print("Dijkstra 1→3:", dijkstra("1", "3"))
print("A* 1→3:", a_star("1", "3"))

print("\nMerkezilik (En Etkili Kullanıcılar):")
for node, deg in merkezilik():
    print(node, "-", G.nodes[node]["isim"], "- Derece:", deg)