print("======================| Menghitung Gaji Pegawai |======================")

# input
nama = input("Nama : ")
gaji_pokok = input("Gaji Pokok : ")
jam_kerja = input("Jam Kerja : ")
jumlah_potongan = input("Jumlah Potongan : ")

# process
upah_kerja = int(jam_kerja) * 10000
total_gaji = int(gaji_pokok) + upah_kerja
gaji_bersih = total_gaji - int(jumlah_potongan)

# output
print("=================================================================")
print("======================| Slip Gaji Pegawai |======================")
print("=================================================================")
print("------> Nama Pegawai    : ", nama)
print("------> Gaji Pokok      : ", gaji_pokok)
print("------> Jam Kerja       : ", jam_kerja)
print("------> Jumlah Potongan : ", jumlah_potongan)
print("------> Upah Kerja      : ", upah_kerja)
print("------> Total Gaji      : ", total_gaji)
print("------> Gaji Bersih     : ", gaji_bersih)
