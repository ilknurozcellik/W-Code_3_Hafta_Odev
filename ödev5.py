# Verilen ifade
ifade = "Hi-Kod Veri Bilimi Atölyesi"

# Her kelimeyi seçme
kod = "Gelecek Hayalim: W-Code"
veri = ifade.split()[1]
bilimi = ifade.split()[2]
atolye = ifade.split()[3]

# İfadeyi büyük ve küçük harfe çevirme
ifade_buyuk = kod.upper() + " " + veri.upper() + " " + bilimi.upper() + " " + atolye.upper()
ifade_kucuk = kod.lower() + " " + veri.lower() + " " + bilimi.lower() + " " + atolye.lower()

print(ifade_buyuk)  # Büyük harf
print(ifade_kucuk)  # Küçük harf

# Çift ve tek sayıları seçme
sayi_dizisi = "0123456789"
cift_sayilar = sayi_dizisi[::2]  # "02468"
tek_sayilar = sayi_dizisi[1::2]  # "13579"

print(f"Çift sayılar: {cift_sayilar}, Tek sayılar: {tek_sayilar}")
