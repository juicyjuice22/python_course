
id = " "
password = " "
id_real = "tebak"
password_real = "0000"
coba = [3,2,1]

while True:
   for x in range(3,0,-1):
      print(f"Anda punya {x} kali coba.")
      id = input ("Masukkan Username Anda: ")
      password = input ("Masukkan password Anda: ")
      if id == id_real and password == password_real:
         print ("--ACCESS GRANTED--")
         break
      else:
         print("--ACCESS DENIED--")
   break

print("Coba nanti lagi.")
