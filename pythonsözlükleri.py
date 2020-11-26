###########################################################################
#
#  clear()	        Sözlükten tüm öğeleri kaldırır
#  copy()	        Sözlüğün bir kopyasını verir
#  fromkeys()	    Belirtilen anahtarlara ve değere sahip bir sözlük verir
#  get()	        Belirtilen anahtarın değerini döndürür
#  items()	        Her anahtar-değer çifti için bir demet içeren bir liste döndürür (listeleme halinde alt alta yazar)
#  keys()	        Sözlüğün anahtarlarını içeren bir liste verir
#  pop()	        Belirtilen anahtara sahip öğeyi kaldırır
#  popitem()	    Son eklenen anahtar / değer çiftini kaldırır
#  setdefault()	    Belirtilen anahtarın değerini döndürür. Anahtar yoksa: anahtarı belirtilen değerle girin
#  update()     	Sözlüğü belirtilen anahtar / değer çiftleriyle günceller
#  values()	        Sözlükteki tüm değerlerin bir listesini verir
#
###########################################################################
#
#
# Sözlük, sıralanmamış, değiştirilebilir ve indekslenmiş bir koleksiyondur.
# Python'da sözlükler küme parantezleriyle yazılır ve anahtarları ve değerleri vardır.
#
#
###########################################################################

print("")
print("")
print("Bejo Kod Yazıyor.")
print("")
print("")

###########################################################################
#
# thisdict Bu Günkü Öncelikli kelimemiz :)
#
###########################################################################

# Bir sözlük oluşturun ve yazdırmaya yarar
print ("1. Tanım Ve Örneği")
thisdict = {
  "Marka": "Ford",
  "Model": "Mustang",
  "Yıl": 2019 
}
print(thisdict)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Bir sözlük oluşturun ve OLUŞTURULAN ŞEYİ YAZDIRMAYA YARAR 
print ("2. Tanım Ve Örneği")
thisdict ={
    "Marka" : "Ford", # Virgül Koymak Önemli Unutma
    "Model" : "Mustang",
    "Yıl"   : 1964
}
x = thisdict["Model"] # Model Türü Yazdırılır
print(x)


#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# 1998 oalrak gösterilen yılı 2020 yapar
print ("3. Tanım Ve Örneği")
thisdict = {
    "Marka" : "Ford", # Virgül Koymak Önemli Unutma
    "Model" : "Mustang",
    "Yıl"   :  1998
}
thisdict["Yıl"] = 2020
print(thisdict)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Koddaki tüm değerleri tek tek alt alta yazdırır.  Yazdırılan kelimeler (Marka, Model, Yıl)
print("4. Tanım ve Örneği")
thisdict= {
    "Marka" : "Ford",
    "Model" : "Mustang", 
    "Yıl"   :  2020  
}
for x in thisdict:
    print(x)
# for x in bu işe yarar

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Değerleri Alt Alta Yazdırır. Yazdırılan kelimeler (Ford, Mustang, 2020 )
print("5. Tanım ve Örneği")
thisdict = {
    "Marka" : "Ford",
    "Model" : "Mustang",
    "Yıl"   : 2020
} 
for x in thisdict:
    print(thisdict[x])

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Values Bir sözcüğün değerlerini döndürmek için kurulur.
print("6. Örnek ve Tanımı")
thisdict = {
    "Marka" : "Ford",
    "Model" : "Mustang",
    "Yıl"   : 2020
}
for x in thisdict.values():
    print(x)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# 2 Döngüyü Şifreler ve değerlerini kullanır. Örneğin çıktı şekli  [Marka Ford, Model Mustang, Yıl 2020]
print("7. Tanım ve Örneği")
thisdict = {
    "Marka" : "Ford",
    "Model" : "Mustang",
    "Yıl"   : 2020
}
for x, y in thisdict.items():
    print(x, y)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Model Kelimesinin İçinde Olup Olmadıgını Kontrol Eder
print("8. Tanım ve Örneği")
thisdict = {
    "Marka" : "Ford",
    "Model" : "Mustag",
    "Yıl"   : 2020
}
if "Model" in thisdict:
    print("Evet 'Model' kelimesi kodun içinde var.")
else:
     print("Hayır 'Mustag' Kelimesi sistemin içinde yok") # Model Kelimesi yoksa bu mesaj çıkar Else Konumuzla ilgili değil ama örnek örnektir :)
# 9. tanımda yani bundan sonraki tanımda örneğini vereceğim.

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Model Kelimesinin İçinde Olup Olmadıgını Kontrol Eder
print("9. Tanım ve Örneği")
thisdict = {
    "Marka" : "Ford", 
    "Model" : "Mustang",
    "Yıl"   : 2020
}
if "model" in thisdict:
    print("Evet 'model' Kelimesi kodun içinde var") # Yukarda Yaptığımız gibi model kelimesi bu sefer yok 
else:
    print("Hayır 'model' Kelimesi kodun içinde yok") # Bu yüzden bu mesaj çıktı if 
# if else örneğide Yapmıs olduk

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Listede Kaç adet satır olduğunu bizlere gösteriyor.
print("10. Tanım ve Örneği")
thisdict = {
    "Model" : "Ford",
    "Marka" : "Mustang",
    "Yıl"   : 2020
}
print(len(thisdict)) # len tekrar burada kullanmış olduk :) saymaya devam

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Listeye Yeni Bir Satır Eklemeye Yarıyor. thisdict["Rengi"]
print("11. Tanım ve Örneği")
thisdict = {
    "Model" : "Ford",
    "Marka" : "Mustang",
    "Yıl"   : 2020
}
thisdict["Rengi"] = "Kırmızı"
print(thisdict)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# pop() Listedeki satırlardan belitrileni silmeye yarar
print("12. Tanım ve Örneği")
thisdict = {
    "Model" : "Ford",
    "Marka" : "Mustang",
    "Yıl"   : 2020
}
thisdict.pop("Model")
print(thisdict)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# python (3.7 Önceki sürümlerde rasgele bir madde kaldırmaya yarıyordu) şimdiki sürümlerde listedeki son madddeyi kaldırır.
print("13. Tanım ve Özelliği")
thisdict = {
    "Model" : "Ford",
    "Marka" : "Mustang",
    "Yıl"   : 2020
}
thisdict.popitem()
print(thisdict)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Belitrilen anahtar kelimeyi listeden kaldırmaya yarar
print("14. Tanım ve Özelliği")
thisdict = {
    "Model" : "Ford",
    "Marka" : "Mustang",
    "Yıl"   : 2020
}
del thisdict ["Model"] # Belirttiğimiz anahtar
print(thisdict)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Tüm listedekileri temizler clear() komutu
print("15. Tanım ve Özelliği")
thisdict = {
    "Model" : "Ford",
    "Marka" : "Mustang",
    "Yıl"   : 2020
}
thisdict.clear()
print(thisdict)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

###########################################################################
#
#
#                     -----Ufak Notlar----
# todo Sözlüğü Kopyala
# *Bir sözlüğü sadece yazarak kopyalayamazsınız gencolar dict2 = dict1 vardır ;)
# ?dict2 sadece referans olur dict1 ve içinde yapılan değişiklikler dict1 de otomatik olarak yapılır.
# !Kopya oluşturmanın yolları vardır, bir yol da yerleşik Sözlük yöntemini kullanmaktır copy() 
#
#
###########################################################################

print("16. Tanım ve Özelliği")
thisdict= {
    "Marka" : "Ford",
    "Model" : "Mustang",
    "Yıl"   : 2020
}
kopyalama = thisdict.copy()
print(kopyalama)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

print("17. Tanım ve Özelliği")
thisdict= {
    "Marka" : "Ford",
    "Model" : "Mustag",
    "Yıl"   : 2020
}
kopyalama = dict(thisdict)
print(kopyalama)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Bu sever 3lü sözlük listesi oluşturduk. 3 farklı gurubu birleştirdik.
print("18. Tanım ve Özelliği")
benimlistem = {
  # 1. Gurup  
    "Araba" : {
    "Marka" : "Ford",
    "Model" : "Mustang",
    "Yıl"   : 2020 
        },
  # 2. Gurup      
    "Araba1": {
    "Marka" : "Nissan",
    "Model" : "QashQai",
    "Yıl"   : 2020 
        },
  # 3. Gurup    
    "Araba2": {
    "Marka" : "Opel",
    "Model" : "Astra",
    "Yıl"   : 2020
        },
}
print(benimlistem)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# 3 sözcuğu olusturduktan sonra diğer 3 sözcüğü oluşturmaya yarar.
print("19. Tanım ve Örneği")
araba = {
  "Marka" : "Ford",
  "Model" : "Mustang",
  "Yıl"   :  2018
}
araba1 = {
  "Marka" : "Nissan",
  "Model" : "QashQai",
  "Yıl"   :  2019
}
araba2 = {
  "Marka" : "Opel",
  "Model" : "Astra",
  "Yıl"   :  2020
}

benimlistem = {
  "araba" : araba,
  "araba1" : araba1,
  "araba2" : araba2
}
print(benimlistem)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

#Önemli notlar 
# Anahtar kelimne dizin değişebilir oldugunu unutma
# Burada Yukardaki Örnekleri Yaptıgımız gibi : [iki nokta] koymuyoruz = [eşittir] kullanıyoruz önemli
print("20. Tanım ve Örneği")
thisdict = dict(marka="Ford", model="Mustang", yıl=2020)
print(thisdict)


###







