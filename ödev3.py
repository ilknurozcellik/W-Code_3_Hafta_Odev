# Kullanıcıdan iki değer alınması
deger1 = float(input("Birinci sayıyı giriniz: "))
deger2 = float(input("İkinci sayıyı giriniz: "))

# Aritmetik işlemler
toplam = deger1 + deger2
fark = deger1 - deger2
carpim = deger1 * deger2
bolum = deger1 / deger2 if deger2 != 0 else "Tanımsız"  # Bölme işlemi sıfıra bölünemez

# Sonuçları yazdırma
print(f"Toplam: {toplam}, Fark: {fark}, Çarpım: {carpim}, Bölüm: {bolum}")
