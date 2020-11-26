###########################################################################
#
#                        Döngüler İçin Python
# Bir dizi üzerinde yineleme yapmak için bir for döngüsü kullanılır 
# (bu bir liste, bir demet, bir sözlük, bir küme veya bir dizedir).
#                           
# Bu, diğer programlama dillerindeki for anahtar kelimesine 
# daha az benzer ve diğer nesne yönelimli programlama dillerinde 
# bulunan bir yineleyici yöntemi gibi çalışır.
# For döngüsü ile bir liste, tuple, set vb. İçindeki her öğe için 
# bir kez olmak üzere bir dizi deyimi çalıştırabiliriz.                           
#
###########################################################################

print("")
print("")
print("Bejo Kod Yazıyor.")
print("")
print("")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

print("1. Örnek ve Tanımı") # belirtilen kelimeleri alt alta yazar
meyveler = ["elma", "armut", "muz"]
for x in meyveler: # x döngü elemanı 
  for a in x:
    print(a)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# x kelimesi olarak belirlediğimiz proffessiyonel kelimesini her harfini alt alta yazar
print("2. Örnek ve Tanımı")
for x in "proffessiyonel":
    print(x)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################














