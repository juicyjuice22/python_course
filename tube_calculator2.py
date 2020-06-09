list = []

class Calculator:
    def __init__(self,radius,height,tanya,hasil): #init isi yang bakal dipake def lainnya
        self.radius = radius
        self.height = height
        self.tanya = tanya
        self.hasil = hasil
        list.append(self)

    def jadi(self):
        if self.tanya == 1:
            self.tanya = "Luas lingkaran alas tabung "
        if self.tanya == 2:
            self.tanya = "Luas permukaan tabung "
        if self.tanya == 3:
            self.tanya = "Volume tabung "
        print(f"Jari-jari tabung {self.radius}, Tinggi tabung {self.height}, {self.tanya} {self.hasil} ")

    @classmethod
    def Ask(cls):
        try:
            radius = float(input("Masukkan jari-jari tabung: "))
            height = float(input("Masukkan tinggi tabung: "))
        except ValueError:
            print("VALUE ERROR!")
        except:
            print("SOMETHING WENT WRONG!")
        else:
            print("1 Hitung luas lingkaran alas\n"
                  "2 Hitung luas permukaan tabung\n"
                  "3 Hitung volume tabung")
            tanya = int(input("Apa yang ingin dihitung? "))
            if tanya == 1:
                hasil = 3.14 * radius * height
                print(f"Luas lingkaran alas tabung adalah: {float(hasil)}")
            elif tanya == 2:
                hasil = (2 * 3.14 * radius * radius) + (2 * 3.14 * radius * height)
                print(f"Luas permukaan tabung adalah: {float(hasil)}")
            elif tanya == 3:
                hasil = 3.14 * radius * radius * height
                print(f"Volume tabung adalah: {float(hasil)}")
            return cls(radius,height,tanya,hasil)


print("\n--TUBE CALCULATOR--")
q0 = input("Ingin menggunakan kalkulator ini?(y/n) ").lower()

while q0 == "y":
    Calculator.Ask()
    repeat = input("\nMasih ingin menggunakan kalkulator ini?(y/n) ").lower()
    if repeat == "n":
        q0 = "n"

print("\n--Usage History--")
for x in list:
    x.jadi()

input("\nType anything to exit. ")
exit()
