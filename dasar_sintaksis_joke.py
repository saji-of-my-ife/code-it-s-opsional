"""
semua sintaks dasar bahasa pemrogaraman terdiri dari:
1. sekeunsial: langkah berurutan
2. percabangan: langkah meloncat jika kondisi terpenuhi
3. perulangan: mengulang langkah yang berkali kali selama/sampai kondisi terpenuhi
"""
#sekuensial
print('ibu berkata,"pergi ke toko"')
print('Budi menjawab,"baik,apa yang haris saya lakukan di toko?"')
print("maka budi berangkat ke toko")
print("dan mulai berbelanja")

# percabangan
jumlah_botol_susu = 178
jumlah_telur = 2430
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")
if jumlah_botol_susu > 0:
    print("budi mengecak harganya,dan ternyata cukup")
    if jumlah_telur == 0:
        print("budi membeli 1 botol susu")
    else:
        print("budi membeli 1 botol susu")
else:
    print("budi tidak jadi membeli 1 botol susu")
if jumlah_telur > 0:
    print("budi juga mengecek harga telur,dan ternyata cukup")
    print("budi membeli 6 butir telur")
else:
    print("budi membeli 6 butir telur")

print("budi pulang ke rumah")
print("menyampaikan hasilnya kepada ibu")