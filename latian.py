nama = "tsaniya nura" 
nim = 240441100080
ipk = 4.00
mahasiswa = True

print("nama saya adalah", nama)
# ini adalah format natural (tipe data sama)
print("nim saya adalah", nim)
print("cita-cita ipk saya adalah", ipk)
print("saya adalah mahasiswa", mahasiswa)

# ini adalah format string (tipe data di ubah menjadi string)
print (f'nim saya adalah {nim}')

# buat program dinamis integer
nama_panjang = str ( input ("nama saya adalah :"))

#  dinamis integer
 
nilai_matematika = 89
nilai_biologi = 79
nilai_kimia = 90
nilai_fisika = 80


penjumlahan = nilai_matematika + nilai_kimia
pengurangan = nilai_matematika - nilai_kimia
perkalian = nilai_matematika* nilai_kimia
pembagian = nilai_matematika /nilai_kimia

print (f' hasil penjumlahan dari matematika dan kimia adalah :{penjumlahan}')
print (f'hasil penjumlahan dari matematika dan kimia adalah : {perkalian}')

usia_masuk_kuliah = int(input('berapa usia andan ?'))
lama_kuliah = int(input("berapa lama anda kuliah (tahun) ?"))

usia_saat_ini = usia_masuk_kuliah + lama_kuliah
tahun_lulus = 2024 + lama_kuliah

print (f'saat ini, saya {nama} berumur {usia_saat_ini}')
print (f'saya {nama} akan lulus pada tahun {tahun_lulus}')
