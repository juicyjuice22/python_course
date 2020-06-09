
id = " "
password = " "
id_real = "tebak"
password_real = "0000"

while id != id_real and password != password_real:
   id = input ("Masukkan Username Anda: ")
   password = input ("Masukkan Password Anda: ")
   if id != id_real and password != password_real:
      print ("--ACCESS DENIED--")
   else:
      print ("--ACCESS GRANTED--")
