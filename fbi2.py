q0_ans = ("0000")
q1_ans = ("abcd")


def q1():
    q1 = input("Confirmation Password: ")
    while True:
        if q1 == q1_ans:
            q2()
            break

        else:
            print("ACCESS DENIED")
            for i in range(2, 0, -1):
                print("\n"
                      f"Attempts Left: {i}")
                q1 = input("Confirmation Password: ")
                if q1 == q1_ans:
                    q2()
                else:
                    print("ACCESS DENIED")
            exit()
        break


def q2():
    print("\n"
          "------------------------\n"
          "-----SEARCHING DATA-----\n"
          "------------------------")
    import time
    x = "."

    def loading():  # () isinya apa yang mau diisi
        for n in range(0, 5):
            print("Loading" + x * n)
            time.sleep(0.75)

    loading()
    loading()
    loading()

    print("\n"
          "------------------------\n"
          "---IDENTIFIED SUSPECT---\n"
          "------------------------")

    people = {"(1)": {
        "Name   : ": "Vladimir",
        "Age    : ": "25",

        "Crime  : ": "SQL Injections"
                     "\n"},
        "(2)": {
            "Name   : ": "Anna",
            "Age    : ": "18",
            "Crime  : ": "Cross-site Scripting"
                         "\n"},
        "(3)": {
            "Name   : ": "Maksim",
            "Age    : ": "35",
            "Crime  : ": "DoS Attack"
                         "\n"}}

    for key, value in people.items():
        print(key)
        for info_key, info_value in value.items():
            print(info_key, info_value)

    q1 = ""
    while True:
        q1 = input("Click 0 to EXIT. ")
        if q1 != "0":
            print("Try Again\n")
        else:
            break

    exit()



print("\n"
      "CYBER'S MOST WANTED")

q0 = input ("Identification Number: ")
while True:
    if q0 == q0_ans:
        q1()
        break

    else:
        print("ACCESS DENIED")
        for x in range (2,0,-1):
            print("\n"
                  f"Attempts Left: {x}")
            q0 = input("Identification Number: ")
            if q0 == q0_ans:
                q1()
            else:
                print("ACCESS DENIED")
        exit()
    break
