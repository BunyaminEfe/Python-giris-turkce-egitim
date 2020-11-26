print("1.len kullanımı")
#Listenin kaç tane elemanı olduğunu gösterir.
liste = ["hasan",35,"bandırma",23.2]
print(len(liste))

print("")

print("2.type kullanımı")
#Listenin hangi veri tipinden olduğunu gösterir.
liste2 = ["Yemek",23,"İstanbul",2.4]
print(type(liste2))

print("")

print("3.list() kullanımı")
#Listenin boş olduğunu belirtir.
liste3 = print(list())

print("")
print("4.list() komutu ile string ifadeyi liste haline çevirme")
liste4 = print(list("Berkay"))

print("")
print("5.değişken[sayı] komutu")
liste5 = [3,4,5,6,7,8,9,10]
print(liste5[0])

print("")
print("6.değişken[sayı] komutu")
liste6 = [3,4,5,6,7,8,9,10]
print(liste6[-1])

print("")
print("7.Listenin sondan başlamasını sağlar.")
liste6 = [3,4,5,6,7,8,9,10]
print(liste6[::-1])

print("")
print("8.Liste Birleştirme")
liste7 = [1,2,3]
liste8 = [4,5,6]
toplam = liste7 + liste8
print(toplam)

print("")
print("9.Liste Değiştirme")
liste9 = [1,2,3]
liste9 = liste9 * 3
print(liste9)

print("")
print("10.Listedeki Değişkeni Değiştirme")
liste10 = [4,5,6]
liste10[1] = 10
print(liste10)

print("")
print("11.Listedeki Değişkenleri Değiştirme")
liste11 = [1,2,3]
liste11[:2] = [10,11]
print(liste11)

print("")
print("12.append Metodu = Listeye istenilen veriyi ekler.")
liste12 = [1,2,3,4]
liste12.append(5)
print(liste12)

print("")
print("13.pop Metodu = Listeyden istenilen veriyi siler.Not(Eğer elemena hiçbir değer verilmezse sondaki elemanı siler.)")
liste13 = [1,2,3,4]
liste13.pop(0)
print(liste13)

print("")
print("14.sort Metodu = Listedeki sayıları baştan sona sıralar.(String ifade tanımlarsak alfabetik sıraya göre sıralar.)")
liste14 = [5,2,35,24,42,11,67,51]
liste14.sort()
print(liste14)

print("")
print("15.sort(reverse = True) = Listedeki Sayıları Sondan başa doğru sıralar.")
liste15 = [5,2,35,24,42,11,67,51]
liste15.sort(reverse=True)
print(liste15)

print("")
print("16.İç İçe Listelerde istenilen değere ulaşma")
liste16 = [[1,2],[3,4],[5,6]]
print(liste16[1][1])

print("")
print("17.Demetler(Tuplelar)")
liste17 = (1,2,3,4,5,6,7)
print(type(liste17))

print("")
print("18.Count Fonksiyonu = Bir değişkenin Tuple içinde kaç defa geçtiğini gösterir.")
liste18 = (1,1,1,1,1,2,2,2,3,3)
print(liste18.count(1))

print("")
print("19.İndex Fonksiyonu = Varolan bir değişkenin kaçıncı indekste olduğunu belirtir.")
liste19 = ("Python","Php","C","Java")
print(liste19.index("Python"))

print("")
print("20.Sözlük Veri Tipi")
liste20 = {"bir":1,"iki":2,"üç":3,"dört":4,"beş":5}
print(type(liste20))

print("")
print("21.Sözlükte bulunan değişkeni bulma")
liste21 = {"bir":1,"iki":2,"üç":3,"dört":4,"beş":5}
print(liste21["iki"])

#