import random

base="abcdefghijklmnopqrstuvwxyz"

passw=""
x=int(input("cuantas contraseñas quieres?"))
h=int(input("de cuantos caracteres?"))

for i in range (h ):
  for j in range(x):
    passw=passw+random.choice(base)
  print("password" ,passw)

  passw=""
  
  input()

