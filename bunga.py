list = []

class Flower:
    def __init__(self,name,petals,price):
        self.name = name
        self.petals = petals
        self.price = price
        list.append(self)

    def hasil(self):
        print("Bunga bernama " ,self.name, ", memiliki kelopak sejumlah " ,self.petals, ", memiliki harga " ,self.price, " rupiah.")

    @classmethod
    def ask(cls): #engga pakai koma koma krn gabisa...
        name = input("Masukkan nama bunga: ")
        petals = input("Masukkan jumlah kelopak bunga: ")
        price = input("Masukkan harga: ")
        return cls(name,petals,price)

q0 = "y"

while q0 == "y":
    Flower.ask()
    repeat = input("Input data lagi?(y/n) ")
    if repeat == "n":
        q0 = "n"

for x in list:
    x.hasil()
