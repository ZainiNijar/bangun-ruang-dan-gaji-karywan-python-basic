print("======================| Menghitung Volume Bola |======================")

phi = float(3.14)
jari_jari = int(input("Jari-jari : "))

if jari_jari % 7 == 0:
    phi = float(22/7)

volume = float((4 / 3) * phi * jari_jari * jari_jari * jari_jari)

print("Volume Bola : ", round(volume, 2))
