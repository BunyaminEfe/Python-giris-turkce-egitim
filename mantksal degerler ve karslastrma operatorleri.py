#                                   MANTIKSAL DEĞERLER
#Mantıksal değerler ya da ingilizce adıyla boolean değerler aslında Pythondabir veri tipidir.
#İki değere sahiptir "True" ve "False".
#Alt tarafta bunların örnekleri olucak
print ("1. Tanım Ve Örneği")
a = True
print(type(a))

print("")

b = False
print(type(b))

#Görüldüğü üzere ikisininde sınıfı bool çıkıyor bir fark yok.

print("")

#Pyhtonda bir değişkenin değerini sonradan belirlemek istiyorsanız "None" (atanmamış anlamında) değerine eşitleyebilirsinizi.
print ("2. Tanım Ve Örneği")
a = None #Daha değer atamadık.
print(a)

print("")


print ("3. Tanım Ve Örneği")
a = 4 #Şimdi değer veriyoruz
print(a)

print("")



print ("4. Tanım Ve Örneği")
#                              KARŞILAŞTIRMA OPERATÖRLERİ

#  == iki değer biribirine eşitse true. iki değer birbirine eşit değilse false
print("2" == "2")
print("MEHMET" == "AHMET")

print("")

# !=  iki değer birbirine eşit değilse True , eşit ise False

print ("5. Tanım Ve Örneği")


print("2" != "2")  #değerler eşit olduğu için false oldu
print("MEHMET" != "AHMET") #değerler eşit olmadığı için true oldu

print("")



print ("6. Tanım Ve Örneği")
#   > soldaki değer sağdakinden büyükse true ,soldaki değer sağdakinden küçükse false.

print("1" > "2")  # küçük olduğu için false 
print("5" > "4")  #büyük olduğu için true 

print("")



print ("7. Tanım Ve Örneği")
#bu operatöre ek bilgi olarak kelimeleride kullanabilirsiniz alfabeye göre sıralar.
print("zebra" > "armut")
print("elma" > "kavun")

print("")



print ("8. Tanım Ve Örneği")
#   < soldaki değer sağdakinden küçükse True , soldaki değer sağdakinden büyükse False. 
print("2" < "3")  #küçük olduğu için true
print("5" < "1")  #büyük olduğu için false

print("")


print ("9. Tanım Ve Örneği")

#bu operatöre ek bilgi olarak kelimeleride kullanabilirsiniz alfabeye göre sıralar.

print("erik" < "karpuz") # e harfi k den önce geldiği için true
print("zürafa" < "deve") # z harfi d den sonra geldiği için false

print("")



print ("10. Tanım Ve Örneği")
# >= soldaki değer sağdakinden büyükse ya da eşitse true , ikisinden birisi olmazsa false
print("15" >= "15") #eşit olduğu için true
print("23" >= "12") #büyük olduğu için true
print("14" >= "13") #ne büyük ne de eşit olmadığı için false

#bu operatöre ek bilgi olarak kelimeleride kullanabilirsiniz alfabeye göre sıralar.

print("")


print ("11. Tanım Ve Örneği")
# <= soldaki değer sağdakinden küçükse ya da eşitse true , ikisinden birisi olmazsa false
print("37" <= "37") #eşit olduğu için true
print("46" <= "54") #küçük olduğu için true 
print("57" <= "55") #büyük olduğu için false



