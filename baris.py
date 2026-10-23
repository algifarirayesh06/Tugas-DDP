# Meminta input jumlah baris dari pengguna
jumlah_baris = int(input("Masukkan jumlah baris: "))

# Menggunakan for loop dengan range untuk mencetak pola bintang
for i in range(1, jumlah_baris + 1):
    print("*" * i)