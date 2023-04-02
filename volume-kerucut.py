print("======================| Menghitung Volume Kerucut |======================")

phi = float(3.14)
jari_jari = int(input("Jari-jari : "))
tinggi = int(input("Tinggi : "))

if jari_jari % 7 == 0:
    phi = float(22/7)

volume = float((1 / 3) * phi * jari_jari * jari_jari * tinggi)

print("Volume Kerucut : ", round(volume, 2))
