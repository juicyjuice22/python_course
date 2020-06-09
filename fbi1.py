print("\n"
      "CYBER'S MOST WANTED")

q0 = input ("Identification Number: ")
q0_ans = ("9534")

if q0 != q0_ans:
    print("ACCESS DENIED. YOU ARE PROHIBITED TO ACCESS THIS DATA.")
else:
    print("\n"
          "------------------------\n"
          "-----SEARCHING DATA-----\n"
          "------------------------")
    import time
    x = "."
    def loading(): #() isinya apa yang mau diisi
        for n in range (0,5):
            print("Loading" + x * n)
            time.sleep(0.75)
    loading()
    loading()
    loading()

    print ("\n"
           "------------------------\n"
           "---IDENTIFIED SUSPECT---\n"
           "------------------------")

    people = {"(1)" : {
        "Name   : ": "Vladimir",
        "Age    : ": "25",
        "Crime  : ": "SQL Injections"
    "\n"},
    "(2)" : {
        "Name   : ": "Anna",
        "Age    : ": "18",
        "Crime  : ": "Cross-site Scripting"
    "\n"},
    "(3)" : {
        "Name   : ": "Maksim",
        "Age    : ": "35",
        "Crime  : ": "DoS Attack"
    "\n"}}

    for key,value in people.items():
        print (key)
        for info_key,info_value in value.items():
            print (info_key,info_value)

    q1 = ""
    while True:
        q1 = input("Click 0 to EXIT. ")
        if q1 != "0":
            print("Try Again\n")
        else:
            break
