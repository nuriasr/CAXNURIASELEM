import datetime

dia= datetime.date.today()

print(dia)

w=dia.weekday()+1

if (w==0):
  print('feliz domingo')

elif (w==1):
  print("boo es lunes")

elif (w==2):
  print("hoy es martecito de cafecito")

elif (w==3):
  print("miercoles de plaza")

elif (w==4):
  print("jueves ya casi viernes")

elif (w==5):
  print("wooooooo ya es viernes")

else:
  print("yahoo es sabado")














