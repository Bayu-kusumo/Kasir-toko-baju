import datetime
waktu = datetime.datetime.now()

#input Harga baju
print ("===========Jumlah Baju=============")
def hitung_baju(jumlah_baju):
    total_baju = 0
    for urutan_baju in range(1, jumlah_baju + 1):
        harga_baju = int(input(f"Masukkan Harga Baju ke-{urutan_baju}: "))
        total_baju += harga_baju
    return total_baju
jumlah_baju = 0

while jumlah_baju < 1:
    jumlah_baju = int(input("Silahkan masukkan jumlah baju: "))

total_harga = hitung_baju(jumlah_baju)
print ("==================================")

#daftar ukuran dan harga tambahan
harga_baju = {
    "M" : 0,
    "S" : 0,
    "X" : 5000,
    "XL" : 12000,
    "XXL" : 20000
}

#Menampilkan daftar harga
print ("============== Daftar Harga Ukuran Baju ==============")
for i in harga_baju:
    print (f"Ukuran : {i} \t harga tambahan : Rp{harga_baju[i]}")
print ("Beli 1 dapat Diskon 10%, 2 dapat Diskon 15%")
print ("Jika lebih dari 2 dapat diskon 20%")
print ("======================================================")

beli = input("Pilih Ukuran Baju: ")

bayar = total_harga + jumlah_baju * harga_baju[beli]

# Hitung Harga diskon
if jumlah_baju == 1:
    diskon = bayar * 0.10
    harga = bayar - diskon
elif jumlah_baju == 2:
    diskon = bayar * 0.15
    harga = bayar - diskon
elif jumlah_baju > 2:
    diskon = bayar * 0.10
    harga = bayar - diskon
else :
    print ("Maaf Jumlah yang di masukkan tidak valid")
print("")
print("")
print("")
print("")
print("")

#menampilkan nota dan memasukkan nilai uang
print("==================== Nota ====================")
print (waktu)
print ("Yogyakarta")
print (f"Diskon yang didapatkan : Rp{diskon}")
print (f"Total Harga            : Rp{harga}")
nilai_pembayaran = int(input("Uang yang diberikan    : Rp"))

if nilai_pembayaran < harga:
    print("===============================================")
    print("    Maaf Nilai yang dimasukkan tidak valid    ")
    print("===================ERROR=======================")
else :
    kembalian = nilai_pembayaran - harga

    print (f"Kembalian              : Rp{kembalian:.2f}")
    print ("")
    print ("Terima Kasih telah berbelanja di toko kami")
    print("===============================================")