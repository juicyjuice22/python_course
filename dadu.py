print("\n"
      "--DICE ROLL SIMULATOR--\n")

q0 = "y"

while q0 == "y":
        for x in range(int(input("How many dice would you like to roll? "))):
            ans = random.randint(1,6)
            print (f"Dice {x+1} rolled a {ans}")
            time.sleep(0.5)
        q0 = input("Do you want to start rolling the dice again?(y/n): ")
else:
    print("Bye!")
    exit()
