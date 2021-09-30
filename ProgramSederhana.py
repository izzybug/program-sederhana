# Deklariskan fungsi operasi
def fungsi_total_nilai(nilai_harian, nilai_uts, nilai_uas):
    nilai_harian = int(nilai_harian) * 0.3
    nilai_uts = int(nilai_uts) * 0.3
    nilai_uas = int(nilai_uas) * 0.4
    
    nilai_total = nilai_harian + nilai_uts + nilai_uas
    return nilai_total

# Deklarasikan Fungsi Percabangan
def fungsi_percabangan(nilai):
    nilai_huruf = ''
    if (nilai >= 0 and nilai < 20):
        nilai_huruf= 'E'
    elif (nilai >= 20 and nilai < 40):
        nilai_huruf = 'D'
    elif (nilai >= 40 and nilai < 60 ):
        nilai_huruf = 'C'
    elif (nilai >= 60 and nilai < 80):
        nilai_huruf = 'B'
    elif (nilai >= 80 and nilai < 100):
        nilai_huruf = 'A'
    return nilai_huruf

# Deklarasikan Fungsi Perulangan
def fungsi_perulangan():
    nilai_hasil_perulangan = 0
    for i in range(1,3):
        print('---Nilai ke',i,'---')
        nilai_harian = input('Nilai Harian: ')
        nilai_uts = input('Nilai UTS: ')
        nilai_uas = input('Nilai UAS: ')
        
    # Pemanggilan Fungsi Penjumlahan
    nilai_hasil_perulangan +=(int(fungsi_total_nilai(nilai_harian, nilai_uts, nilai_uas)))
    
    return nilai_hasil_perulangan/i

nilai_total = fungsi_perulangan()

print('---Total Nilai---')
print('Total nilai yang didapat: ',nilai_total)

# cetak percabangan
print('Total Nilai Dalam Huruf: ', fungsi_percabangan(nilai_total))