print("ingresa nombre artículo no 1:" )
pepe=input()
print("ingresa precio del artículo: ")
precio=(int(input()))

print("ingresa nombre artículo no. 2: ")
chucho=input()
print("ingresa precio del artículo: ")
chucho2=(int(input()))

print("ingresa nombre artículo no. 3: ")
chicharo=input()
print("ingresa precio del artículo: ")
chicharo2 =(int(input()))

print("ingresa nombre artículo no. 4: ")
gisante=input()
print("ingresa precio del artículo: ")
gisante2 =(int(input()))

print("ingresa nombre artículo no. 5: ")
yakult=input()
print("ingresa precio del artículo: ")
yakult2 =(int(input()))

suma=(precio+chucho2+chicharo2+gisante2+yakult2)

print("subtotal es : ",suma)

iva=(suma*0.16)

print("total es: ",suma+iva)