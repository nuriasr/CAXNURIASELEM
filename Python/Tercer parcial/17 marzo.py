while True:
  passw=input("ingresa el password: ")
  if(passw=="reprobados"):
    break

print("fin deljuego")


num=0
for x in range (20):
  num=num+3
  if (num==15):
    continue  

  print(num)