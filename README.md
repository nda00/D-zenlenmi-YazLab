# D-zenlenmi-YazLab




----------------------------------------

SOSYAL AĞ ANALİZİ UYGULAMASI RAPORU
#1. Proje Bilgileri

Proje Adı: Sosyal Ağ Analizi Uygulaması
Ders: Graf Algoritmaları / Veri Yapıları
Hazırlayan: …NidaTat…181307068……01.01.2026………


#2. Giriş (Problemin Tanımı)

Günümüzde sosyal medya ve benzeri platformlarda kullanıcılar arasında çok sayıda bağlantı bulunmaktadır. Bu bağlantılar bir ağ yapısı oluşturmaktadır. Bu ağ yapısı grafik (graf) veri yapısı ile modellenebilir.

Bu projede, kullanıcılar düğüm (node), kullanıcılar arasındaki bağlantılar ise kenar (edge) olarak ele alınmıştır. Amaç, bu sosyal ağı bir grafik yapısı ile modellemek ve grafik algoritmaları kullanarak ağ üzerindeki ilişkileri analiz etmektir.

Proje sayesinde grafik veri yapıları, algoritmalar ve görselleştirme konuları uygulamalı olarak öğrenilmiştir.

#3. Kullanılan Teknolojiler

Python programlama dili

NetworkX (graf işlemleri için)

Matplotlib (graf çizimi ve görselleştirme için)

#4. Graf Modeli ve Yapısı

Projede yönsüz ve ağırlıklı bir graf kullanılmıştır.

Düğümler (Node): Kullanıcıları temsil eder

Kenarlar (Edge): Kullanıcılar arasındaki bağlantıları temsil eder

Ağırlıklar: Kullanıcıların aktiflik değerleri arasındaki farka göre hesaplanır

Kenar ağırlığı şu şekilde hesaplanmıştır:

İki kullanıcının aktiflik farkı alınır ve +1 eklenir.

Bu sayede benzer kullanıcılar arasındaki mesafe daha küçük olur.

#5. Gerçeklenen Algoritmalar
#5.1 BFS (Genişlik Öncelikli Arama)

BFS algoritması, bir düğümden başlayarak komşu düğümleri seviye seviye dolaşır. Bu projede BFS kullanılarak bir kullanıcıdan erişilebilen tüm kullanıcılar bulunmuştur.

Kuyruk (queue) yapısı kullanılmıştır.

Önce yakın düğümler ziyaret edilir.
Literatür:
BFS algoritması, kısa yol mantığını anlamak ve graf üzerinde katmanlı gezinme yapmak için
 kullanılmaktadır.

#5.2 DFS (Derinlik Öncelikli Arama)

DFS algoritması, bir düğümden başlayarak mümkün olduğunca derine iner. Bu projede DFS ile kullanıcılar arasındaki bağlantıların derinlemesine incelenmesi sağlanmıştır.
Literatür:
 DFS algoritması, grafiklerin yapısını incelemek ve bağlı bileşenleri bulmak için yaygın
 olarak kullanılan temel bir algoritmadır.

**Zaman Karmaşıklığı:**  
O(V + E)

mermaid
flowchart TD
A[Başlangıç Düğümü] --> B[Düğümü Ziyaret Et]
B --> C[Komşuya Git]
C --> B
Zaman Karmaşıklığı: O(V + E) ne demek?
Bu ifade şunu anlatır:
V (Vertex) → düğüm sayısı
E (Edge) → bağlantı (kenar) sayısı
O(V + E) demek:
Algoritma çalışırken tüm düğümleri (V) ve tüm bağlantıları (E) en fazla birer kez dolaşır.
  Yani:
Düğüm sayısı artarsa → süre artar
Bağlantı sayısı artarsa → süre artar
Ama gereksiz tekrar yok, bu yüzden verimli kabul edilir.

 

Yığın (stack) mantığı ile çalışır.

Bir yol bitmeden geri dönmez.

#5.3 Dijkstra Algoritması

Dijkstra algoritması, iki düğüm arasındaki en kısa yolu bulmak için kullanılmıştır. Bu projede kenar ağırlıkları kullanılarak en kısa yol hesaplanmıştır.

Ağırlıklı graf üzerinde çalışır.

En düşük maliyetli yolu bulur.

#5.4 A* (A-Star) Algoritması

A* algoritması, Dijkstra algoritmasına ek olarak sezgisel (heuristic) bir fonksiyon kullanır. Bu sayede hedef düğüme daha hızlı ulaşmayı amaçlar.

Projede A* algoritması NetworkX kütüphanesi kullanılarak basit bir heuristic ile uygulanmıştır.

#5.5 Merkezilik (Degree Centrality)

Merkezilik hesaplamasında her düğümün sahip olduğu bağlantı sayısı hesaplanmıştır. En fazla bağlantıya sahip düğümler en etkili kullanıcılar olarak değerlendirilmiştir.

Sonuçlar sıralanarak en etkili kullanıcılar listelenmiştir.

#5.6 Welsh–Powell Graf Renklendirme

Welsh–Powell algoritması kullanılarak komşu düğümlerin farklı renklere boyanması sağlanmıştır.

Bu sayede:

Topluluklar daha net görülmüştür

Graf görsel olarak daha anlaşılır hale gelmiştir

#6. Görselleştirme

Graf yapısı Matplotlib kullanılarak çizilmiştir.

Düğümler farklı renklerle gösterilmiştir

Kenar ağırlıkları grafik üzerinde yazdırılmıştır

Görselleştirme sayesinde algoritma sonuçları daha anlaşılır hale gelmiştir

Bağlı Bileşenlerin Tespiti
Graf üzerinde birbiriyle bağlantılı olan düğüm grupları bağlı bileşen olarak tanımlanır.
 Bu projede graf üzerinde bağlı bileşenler tespit edilerek
 ayrık topluluklar belirlenmiştir.
Bağlı bileşenler sayesinde:
Sosyal ağdaki kopuk gruplar tespit edilmiştir
Topluluk yapısı daha net görülmüştür


#7. Testler ve Sonuçlar

Küçük ölçekli bir graf (4 düğüm) üzerinde testler yapılmıştır.

BFS ve DFS algoritmaları doğru şekilde çalışmıştır

Dijkstra ve A* algoritmaları en kısa yolu bulmuştur

Merkezilik hesaplamaları beklenen sonuçları vermiştir

Renklendirme işlemi başarılı şekilde uygulanmıştır

#8. Sonuç ve Değerlendirme

Bu projede grafik veri yapıları ve temel grafik algoritmaları başarıyla uygulanmıştır. Sosyal ağlar üzerinde analiz yapabilmek için grafiklerin ne kadar önemli olduğu görülmüştür.

Proje, algoritmaların çalışma mantığını anlamak ve görselleştirmek açısından faydalı olmuştur.

Uygulama Açıklamaları, Testler ve Sonuçlar

Uygulama çalıştırıldığında graf ekranda görsel olarak gösterilmektedir.
 Kullanıcılar düğümlere tıklayarak kullanıcı bilgilerini görebilmektedir.
BFS, DFS, Dijkstra ve A* algoritmaları kullanıcı tarafından çalıştırılmıştır.
 Küçük ve orta ölçekli graflar üzerinde testler yapılmıştır.
Algoritmaların tamamı doğru sonuçlar vermiş ve makul sürelerde çalışmıştır.

Hata Kontrolleri
Projede hatalı veri girişleri engellenmiştir.
Aynı düğüm tekrar eklenemez
Bir düğüm kendisiyle bağlantı kuramaz (self-loop)
Var olmayan düğümler arasında bağlantı oluşturulamaz
Bu kontroller sayesinde sistem daha güvenli hale getirilmiştir.





# https://github.com/nda00/Social-network.git

# https://github.com/nda00/D-zenlenmi-YazLab.git
