#comentarios:son lineas de codigo que no se ejecutan y sirven para dejar pistas o exp de lo que hiciste 

#variables y constantes

#variable: es un dato que puede VARIAR en algun momento

edad=10

edad=edad+1

#constante deberia ser un dato que NO cambia bajo la ninguna circumstancia 

pi=3.1416

#print()envia informacion del CODIGO a la PANTALLA del USUARIO

print(4)
print("hola")
print('adios')
print(pi)

#la informacion no se guarda en memoria 
print(5+5)

#
print("tienes", edad, "años")
print(edad, pi)

#operadores matematicos te puede permite hacer operaciones matematicas +suma -resta *multp /div

a=4.56
b=2

suma=a+b
resta=a-b
mul=a*b
div=a/b

print(suma, resta, mul, div)

#while() permite repetir un codigo SIEMPRE que una condicion ocurra 

#while True:siempre que pueda ejecuta el codigo, siempre puede

#identacion:es un espacio(s) donde le indicamos al programa que ciertas lineas pertenecen a una estructura 

while True:
  print('hola')
  print('adios')

#while (condicion): y esta requiere que una condicion se cumpla para funcionar

#operadores o comparadores logicos: 
#>< mayor on menor que 
#==identico o igual 
#!=diferente que 
#>= o <= ,mayor o igual /// menor o igual 

vidas=5
while (vidas>0):
  print('eres un campeon')
  vidas=vidas-1
  print('nfrfoshbui')


#input()permite al USUARIO ingresar info el codigo no avanza hasta que preciones enter 

print('cuantos libros haz leido')
libro=input()
print('haz leido', libro, 'libros')

pelis=input('cuantas peliculas haz visto este año')
print('has visto', pelis,'peliculas')

# el input solo mete letras o strings no son numeros 

print(libro+peli)

#int(input()) permite que la informacion que se ingrese se lea como numeros, solo funciona con numeros 

print('cuantos libros has leido?')
libro=int(input())
print('has leido', libro,'libros')

print('cuantas pelisculas has visto este año?)
print('has visto', pelis,'peliculas'

print(libro+pelis)










