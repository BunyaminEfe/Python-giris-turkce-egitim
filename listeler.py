############################################################################################
# Yeni Öğreneceğimiz terimler
# Thislist
# for x in [ 10 Tanımda örneği var ]
# remove()
# pop()
# del
# clear()
# copy()
# list()
############################################################################################


print("Merhaba Ben Bejo")
# Lislere Örneklerine Başlıyoruz

### Dokunma
print("")
### Dokunma



# Basit Listeleme İşlemi
print("1. Örnek ve Tanımı")
thislist = ["elma", "armut", "erik", "kiraz"]  # köşeli parantezlerde olmak üzere hepsini alır.
print(thislist) 




### Dokunma
print("")
### Dokunma




# Listedeki seçilen sıradaki kelimeyi yazdırır
print("2. Örnek ve Tanımı")
thislist = ["karpuz", "anans", "muz", "kayısı"] # raklar 0, 1, 2, 3.. . olarak devam eder. 
print(thislist[2]) # 2 nin yerine yazacağınız rakama göre karşılık gelen kelimeyi yazar.





### Dokunma
print("")
### Dokunma





# ilk baştaki kelimeden -1 kelime geriye gider 
print("3. Örnek ve Tanımı")
thislist = ["kaju", "top", "kale", "silah"]
print(thislist[-1]) #rakamı ne kadar arttırıtsak o kadar geriye doğru gider.



### Dokunma
print("")
### Dokunma





# 3. değer dahil değil sonrakı 5. değere kadar olan kelimeler 5. değer dahil
print("4. Örnek ve Tanımı")
thislist = ["kaleci","hastane","para","kalem","kağıt","silgi","çakmak","kitap","ayraç"]
print(thislist[3:5])



### Dokunma
print("")
### Dokunma



# ilk 3 kelimeyi alır. 
print("5. Tanım ve Örneği")
thislist = ["klavye", "ekran", "fare", "ram", "SSD", "fan", "ekran kartı"]
print(thislist[:3]) # buradaki rakamı ne kadar arttırısak o kadar cok kelime seçer




### Dokunma
print("")
### Dokunma





# ilk 2 kelimeyi almaz 
print("6. Tanım ve Örneği")
thislist = ["staj", "araba", "ev", "mülk", "bisiklet", "insan", "eşya"]
print(thislist[2:])




### Dokunma
print("")
### Dokunma



# len lsitenin kaç tane elemanı oldugunu gösterir
print("7. Tanım ve Örneği")
liste = ["staj", "araba", "ev", "mülk"]
print(len(liste))    # önemli olan kelime len





### Dokunma
print("")
### Dokunma





# Negatif index lemedir listenin sonunda başlamak denektir
# Son Ögenin -1 sahip olur 
print("8. Tanım Ve Örneği")
thislist = ["elmas", "yakut", "kömür", "zümrüt", "bor", "mermer", "altın", "toprak", "mineral"]
print(thislist[-4:-1])



### Dokunma
print("")
### Dokunma



# Listeye thislist[1] Kelimeyi eklememizi sağlıyor
print("9. Tanım ve Örneği")
thislist = ["merhaba", "nasılsın", "iyi misin", "hava"]
thislist[1] = "Bejo Kod Yazıyor" # Bukelime lsiteye giriyor.
print(thislist)




### Dokunma
print("")
### Dokunma


# Kelimeleri alt akta sıralamaya yarar 
print("10. Tanım ve Örneği")
thislist = ["araba", "kamyon", "uçak", "jet"]
for x in thislist:
 print(x) # boşluk bırakmak önemli yoksa kod çalışmıyor sebebni öğren.

#Bir döngü kullanarak liste öğeleri arasında geçiş yağmamızı sağlar for döngüsü



### Dokunma
print("")
### Dokunma


# len kullanarak listedeki öge sayısını öğrenmemize yarar
print("11. Tanım Ve Örneği")
thislist =["at", "inek", "koyun", "eşek"]
print(len(thislist))



### Dokunma
print("")
### Dokunma



# append listenin sonuna belirlediğimiz ögeyi ekler 
print("12. Tanım Ve Örneği")
thislist = ["kırmızı", "mor", "sarı"]
thislist.append("turuncu")
print(thislist)




### Dokunma
print("")
### Dokunma


#  listede belirtilen ögenin olup olmadıgını belirlemek için in kullanılır
print ("13. Tanım Ve Örneği")
thislist = ["armut", "muz", "elma", "kayısı"]
if "armut" in thislist:
  print("Evet, 'armut' meyveler listesinde")




### Dokunma
print("")
### Dokunma



# Belirtilen dizine bir öğe eklemek için, insert () kodunu kullanırız
print ("14. Tanım Ve Örneği")
thislist = ["cem", "ulaş", "demir",]
thislist.insert(3,"çok fensaısn")
print(thislist)




### Dokunma
print("")
### Dokunma




# remove belirtilen kelimeyi listeden çıkartmak için gerekli olacak 
print ("15. Tanım Ve Örneği")
thislist = ["kamera", "mikrafon", "klavye", "fare"]
thislist.remove("kamera")
print(thislist)




### Dokunma
print("")
### Dokunma





# listedeki son ögeyi veya belirtilen diziyi öegeyi kaldirir
print ("16. Tanım Ve Örneği")
thislist = ["elma", "armut", "karpuz", "kayısı"]
thislist.pop()
print(thislist)







### Dokunma
print("")
### Dokunma





#del belitrilen anahtar veya index kaldırmaya yarar
print("17. Tanım ve Örneği")
thislist = ["araba", "motor", "tekerlek", "jant"]
del thislist[0]
print(thislist)





### Dokunma
print("")
### Dokunma




# anahtar ve kelimeyi direk silmeye yarar
print("18. Tanım ve Örneği")
thislist = ["Ali", "Baran", "Bünyamin"]
del thislist
print("Burası Boş değer çıkıyor açıklamayı oku ")






### Dokunma
print("")
### Dokunma


# list kullanrak listenin bırk opyasını olusturulabiliyor
print("19. Tanım ve Örneği")
thislist = ["ev", "araba", "koltuk", "sandalye"]
listele = thislist.copy()
print(listele)




### Dokunma
print("")
### Dokunma



# İki veya daha fazla listeyi birleştirmeye yarar
print("20. Tanım ve Örmeği")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)





### Dokunma
print("")
### Dokunma




# List2'yi list1'e ekleyin
print("21. Tanım ve Örmeği")
list1 = ["a", "b", "c"]
list2 = ["1, 2, 3"]
for x in list2:
  list1.append(x)
print(list1)




### Dokunma
print("")
### Dokunma




# extend()List1'in sonuna list2 eklemek için yöntemi kullanın :
print("22. Tanım ve Örmeği")
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)




### Dokunma
print("")
### Dokunma

# yapıcısını yeni bir liste oluşturmak için kullanmak da mümkündür .
print("23. Tanım ve Örmeği")
thislist = list(("elma", "armut", "kavun")) # 2 tane parentez var önemli 
print(thislist)
































