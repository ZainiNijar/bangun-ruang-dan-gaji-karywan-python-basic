print("======================| Menghitung Volume Limas Segi Empat |======================")

panjang_alas = int(input("Panjang Alas : "))
lebar_alas = int(input("Lebar Alas : "))
tinggi = int(input("Tinggi Limas Segi Empat : "))

volume = float((float(1 / 3) * panjang_alas * lebar_alas) * tinggi)

print("Volume Limas Segi Empat : ", round(volume, 2))
