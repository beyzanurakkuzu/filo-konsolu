# Filo Konsolu (sunum prototipi)

Ankara otobüs filosu için filo konsolu prototipi: 5 bölgeye göre canlı harita, araç listesi, hat izleme,
GPS kopma ve yanlış konum raporu, uyarılar ve kademeli güncelleme ekranı.

- **Veri:** hat çizgileri ve duraklar BusPanel'deki gerçek KML verisinden; bölge ve garaj bilgileri ego.gov.tr
  birim sayfalarından. Araçlar, plakalar, IP'ler, uyarılar ve GPS olayları **örnektir**.
- **Harita:** `index.html` içindeki `window.MAPS_KEY` doluysa Google Maps, boşsa OpenStreetMap verisinden
  çizilen vektör harita kullanılır (© OpenStreetMap katkıcıları).
- **Google Maps anahtarı:** Google Cloud'da yalnız `https://beyzanurakkuzu.github.io/filo-konsolu/*` adresine
  (HTTP referrer) ve yalnız Maps JavaScript API'ye kısıtlanmalı; anahtar sayfa kaynağında görünür.
- Sayfa arama motorlarına kapalıdır (`noindex`).

Rubuplus · 2026

## Yerel ağda HTTPS ile yayınlama

```
python3 serve_https.py          # https://<bu bilgisayarın IP'si>:8443/
```
Sertifika (`cert.pem`, `key.pem`) repoya konmaz; varsayılan klasör `~/StudioProjects/filo-konsolu-sertifika`.
Kendinden imzalı sertifikada tarayıcı ilk girişte uyarı verir. Google Maps anahtarına bu adres de
(ör. `https://192.168.1.202:8443/*`) eklenmelidir.
