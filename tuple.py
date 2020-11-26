###########################################################################
#
#
#Tumple düzenli ve değitrilemez koleksıyondur.
#Pythonda tumple yuvarlak parentezle yazılır
#
#
###########################################################################

print("")
print("")
print("Bejo Kod Yazıyor.")
print("")
print("")

###########################################################################



#####################------------------------------########################


# Demet  Oluşturma İlk Örnek
print("1. Tanım ve Örneği")
thistuple = ("elma", "armut", "patetes")
print(thistuple)


#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

#İlk Diziyi Alır 
print("2. Tanım ve Örneği")
thistuple = ("elma", "armut", "patates")
print(thistuple[1]) #1 olması sebebile


#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Negatif indeksleme -1, sondan başlamak, son öğeye, -2ikinci son öğeye vb
print("2. Tanım ve Örneği")
print(thistuple[-1])

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# üçüncü Dörduncu ve beşinci ögeyi alır
print("3. Tanım ve Örneği")
thistuple = ("elma", "armut", "sebil", "ciger", "elmas", "kömürt", "kivi")
print(thistuple[2:5])

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# -1 dizini hariç -4 dizininden sonrasını alır.
print("3. Tanım ve Örneği")
thistuple = ("katalog", "benzin", "bardak", "kablo", "kulaklık", "aseton", "makas")
print(thistuple[-4:-1])

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################



# Ufak Notlar:
# Tuple Değerlerini Değiştirin
# Bir demet oluşturulduktan sonra değerlerini değiştiremezsiniz. 
# Tuple'lar değiştirilemez veya aynı zamanda adlandırıldığı gibi ondarda değişmezdir.
# Ancak bir çözüm vardır.
# TUple'ı bir listeye dönüştürebilir, listeyi değiştirebilir ve 
# listeyi tekrar bir demete dönüştürebilirsiniz.


###########################################################################

# Değiştirebilmek için demeti bir listeye dönüştürün
print("4. Tanım ve Örneği")
x = ("elma", "muz", "armut")
y = list(x)
y[1] = "kivi"
x = tuple(y)
print(x)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Tumpta elma olup olmadıgını kontrol eder.
print("5. Tanım ve Örneği")
thistuple = ("elma", "muz", "armut")
if "elma" in thistuple:
    print("Evet 'elma' burda")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Ufak Notlar:
# Tumple Uzunlugu
# Bir demetin kaç öğeye sahip olduğunu belirlemek için şu len() yöntemi kullanacağız.

###########################################################################

# Demetteki Öge Sayısını Yazın
print("6. Tanım ve Örneği")
thistuple = ("elma", "armut", "kivi")
print(len(thistuple))

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Tek Öğe ile Grup Oluşturma
print("7. Tanım ve Örneği")
thistuple = ("elma")
print(type(thistuple))

thistuple = ("elma")
print(type(thistuple))

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# İki veya daha fazla grubu birleştirmek için + operatörü kullanabilirsiniz
print("8. Tanım ve Örneği")
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################































