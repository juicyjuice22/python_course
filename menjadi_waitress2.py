pesanan = ["Nasi putih", "Ayam goreng", "Tumis kangkung", "Ikan bawal goreng"]
tambahan = " "
tanya = " "

print("\n"
      "W A R U N G   M A S   B A G U S\n"
      "--PESANAN AWAL--")
for x in range(len(pesanan)):
    print(x+1,pesanan[x])

while True:
    tanya = input("\n"
                  "Apakah Anda ingin menambah pesanan lagi?(y/n): ")
    if tanya == "y":
        tambahan = input("Sebutkan pesanan tambahan Anda: ")
        print ("--PESANAN SEMENTARA--")
        pesanan.append(tambahan)
        for menu in range(len(pesanan)):
            print (menu+1, pesanan[menu])
    elif tanya == "n":
        print ("\n"
               f"Baiklah, total pesanan Anda ada {len(pesanan)} jenis:")
        for menu in range(len(pesanan)):
            print (menu+1, pesanan[menu])
        print ("--TERIMA KASIH--")
        break

    else:
        print ("Anda salah ketik.")
