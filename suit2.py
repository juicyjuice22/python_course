import random

def comp(): #dalam () adalah apa yang mau kita panggil
    choice = random.randint(1, 3)
    if choice == 1:
        choice = "BATU"
        return choice
    if choice == 2:
        choice = "GUNTING"
        return choice
    if choice == 3:
        choice = "KERTAS"
        return choice


def win(choice,ask):
    if choice == "BATU" and ask == "BATU":
        print("==TIE==\n")
    if choice == "BATU" and ask == "GUNTING":
        print("==COMPUTER WINS==\n")
    if choice == "BATU" and ask == "KERTAS":
        print("==YOU WIN==\n")
    if choice == "GUNTING" and ask == "BATU":
        print("==YOU WIN==\n")
    if choice == "GUNTING" and ask == "GUNTING":
        print("==TIE==\n")
    if choice == "GUNTING" and ask == "KERTAS":
        print("==COMPUTER WINS==\n")
    if choice == "KERTAS" and ask == "BATU":
        print("==COMPUTER WINS==\n")
    if choice == "KERTAS" and ask == "GUNTING":
        print("==YOU WIN==\n")
    if choice == "KERTAS" and ask == "KERTAS":
        print ("==TIE==\n")

print("\nCOMPUTER VS HUMAN\n"
      "---Suit Battle---\n")

q0 = "y"

while q0 =="y":
    ask = input("Mau keluarin apa?\n"
                "BATU / GUNTING / KERTAS\n").upper()
    if ask == "BATU" or ask == "GUNTING" or ask == "KERTAS":
        choice_comp = comp()
        print(f"{ask} vs {choice_comp}")
        win(choice_comp,ask)
        q0 = input("Mau main lagi?(y/n) ")
    else:
        print("Gaada pilihannya bro.\n")
else:
    print("Oke, bye!")

