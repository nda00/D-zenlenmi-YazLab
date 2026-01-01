Nida Tat 181307068 01.01.2026
SOSYAL AĞ ANALİZİ UYGULAMASI
1. Proje Bilgileri
Proje Adı: Sosyal Ağ Analizi Uygulaması
2. Giriş (Problem Tanımı ve Amaç)
Günümüzde sosyal medya ve benzeri platformlarda kullanıcılar arasında çok sayıda bağlantı bulunmaktadır. Bu bağlantılar bir ağ (network) yapısı oluşturur. Bu ağ yapıları grafik (graf) veri yapısı kullanılarak modellenebilir.
Bu projede kullanıcılar düğüm (node), kullanıcılar arasındaki ilişkiler ise kenar (edge) olarak ele alınmıştır. Amaç, bu sosyal ağı grafik yapısı ile modellemek ve çeşitli grafik algoritmaları kullanarak ağ üzerindeki ilişkileri analiz etmektir.
Bu çalışma sayesinde grafik veri yapıları, temel grafik algoritmaları ve görselleştirme konuları uygulamalı olarak öğrenilmiştir.
3. Kullanılan Teknolojiler
Python: Programlama dili
NetworkX: Graf oluşturma ve algoritmalar için
Matplotlib: Graf çizimi ve görselleştirme için
4. Graf Modeli ve Yapısı
Projede yönsüz ve ağırlıklı bir graf kullanılmıştır.
Düğümler (Node): Kullanıcıları temsil eder
Kenarlar (Edge): Kullanıcılar arasındaki bağlantıları temsil eder
Ağırlıklar: Kullanıcıların aktiflik değerleri arasındaki farka göre hesaplanır
Kenar ağırlığı şu şekilde hesaplanmıştır:
|aktiflik1 - aktiflik2| + 1
Bu sayede aktiflik değeri birbirine yakın olan kullanıcılar arasındaki mesafe daha küçük olur.
5. Kullanılan Algoritmalar
5.1 DFS (Derinlik Öncelikli Arama)
DFS algoritması bir düğümden başlayarak mümkün olduğunca derine iner. Bir yol bitmeden geri dönmez.
Kullanım Amacı: Kullanıcılar arasındaki bağlantıların derinlemesine incelenmesi
Zaman Karmaşıklığı: O(V + E)
flowchart TD
A[Başlangıç] --> B[Düğümü Ziyaret Et]
B --> C[Komşuya Git]
C --> D{Ziyaret Edildi mi?}
D -- Hayır --> B
D -- Evet --> E[Bitiş]
5.2 Dijkstra Algoritması
Dijkstra algoritması iki düğüm arasındaki en kısa yolu bulmak için kullanılır. Ağırlıklı graflar üzerinde çalışır.
Kullanım Amacı: En düşük maliyetli kullanıcı bağlantısını bulmak
Zaman Karmaşıklığı: O((V + E) log V)
flowchart TD
A[Başlangıç] --> B[Mesafeleri Ata]
B --> C[En Küçük Mesafeli Düğümü Seç]
C --> D[Komşuları Güncelle]
D --> E{Hedefe Ulaşıldı mı?}
E -- Hayır --> C
E -- Evet --> F[Bitiş]
5.3 A* (A-Star) Algoritması
A* algoritması, Dijkstra algoritmasına ek olarak heuristic (sezgisel) bir fonksiyon kullanır. Bu sayede hedef düğüme daha hızlı ulaşmayı amaçlar.
Kullanım Amacı: Hedef kullanıcıya daha hızlı en kısa yol bulmak
Zaman Karmaşıklığı: Heuristic fonksiyona bağlıdır
flowchart TD
A[Başlangıç] --> B[Maliyet + Heuristic Hesapla]
B --> C[En Uygun Düğümü Seç]
C --> D[Komşuları Güncelle]
D --> E{Hedef Bulundu mu?}
E -- Hayır --> B
E -- Evet --> F[Bitiş]
5.4 Merkezilik (Degree Centrality)
Merkezilik hesaplamasında her düğümün sahip olduğu bağlantı sayısı hesaplanır. En fazla bağlantıya sahip düğümler en etkili kullanıcılar olarak değerlendirilir.
5.5 Welsh–Powell Graf Renklendirme
Welsh–Powell algoritması, komşu düğümlerin aynı renge boyanmamasını sağlar.
Amaç: Grafın daha okunabilir hale gelmesi
flowchart TD
A[Düğümleri Sırala] --> B[En Yüksek Dereceliyi Seç]
B --> C[Uygun Rengi Ata]
C --> D[Sonraki Düğüme Geç]
D --> E{Bitti mi?}
E -- Hayır --> B
E -- Evet --> F[Bitiş]
6. Sınıf ve Modül Yapısı
classDiagram
class GraphApp {
+kullanici_ekle()
+baglanti_ekle()
+dfs()
+dijkstra()
+astar()
}

class Kullanici {
id
isim
aktiflik
}

GraphApp --> Kullanici
7. Testler ve Sonuçlar
Küçük ölçekli bir graf üzerinde testler yapılmıştır
DFS algoritması doğru çalışmıştır
Dijkstra ve A* algoritmaları en kısa yolu bulmuştur
Merkezilik hesaplamaları beklenen sonuçları vermiştir
Renklendirme işlemi başarılı olmuştur
8. Sonuç ve Değerlendirme
Bu projede grafik veri yapıları ve temel grafik algoritmaları başarıyla uygulanmıştır. Sosyal ağ analizlerinde grafiklerin ne kadar önemli olduğu görülmüştür.
Başarılar
Algoritmalar doğru çalışmıştır
Görselleştirme başarılıdır
Sınırlılıklar
Küçük ölçekli veri kullanılmıştır
Olası Geliştirmeler
Daha büyük veri setleri eklenebilir
Farklı merkezilik ölçüleri uygulanabilir
Bu raporda neler VAR?
✔ Proje bilgileri
 ✔ Giriş (problem + amaç)
 ✔ Algoritmalar
DFS
Dijkstra
A*
Merkezilik
Welsh–Powell
 ✔ Her algoritma için Mermaid akış diyagramı
 ✔ Sınıf / modül diyagramı (Mermaid)
 ✔ Testler ve sonuçlar





# https://github.com/nda00/Social-network.git

# https://github.com/nda00/D-zenlenmi-YazLab.git
