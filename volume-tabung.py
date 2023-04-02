print("======================| Menghitung Volume Tabung |======================")

phi = float(3.14)
jari_jari = int(input("Jari-jari : "))
tinggi = int(input("Tinggi : "))

if jari_jari % 7 == 0:
    phi = float(22/7)

volume = float(phi * jari_jari * jari_jari * tinggi)

print("Volume Volume Tabung : ", round(volume, 2))
