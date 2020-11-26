print("Bejo Kod Yazıyor")

### Dokunma
print("")
print("")
### Dokunma


#  += => Sayıyı verilen değer kadar arttırır.

print("1. tanımı ve örneği")
sayi1= int (10)
sayi1+=5
print(sayi1)



### Dokunma
print("")
### Dokunma

# // => Sayıyı bölerken küsuratları çıkartarak kesin tam sayı değeri verir.
# 
print("2. tanımı ve örneği")
sayi2= float(16)
sayi3= float(5)
sonuc=sayi2//sayi3
print(sonuc)


### Dokunma
print("")
### Dokunma


# ** => Sayının üssünü bulmaya yarar. a sayınını b ninci kuvveti anlamına gelir

print("3. tanımı ve örneği")
sayi4= int(3)
sayi5= int(4)
sonuc=sayi4**sayi5
print(sonuc)


### Dokunma
print("")
### Dokunma



# % => Sayının bölümünden kalanı verir.

print("4. tanımı ve örneği")
sayi6= int(7)  # A sayisi 
sayi7= int(2)  # B sayisi 
sonuc=sayi6 % sayi7
print(sonuc) # bolumden çikan kalan sonuç.


### Dokunma
print("")
### Dokunma


# sayi **=0.5 => Sayının karekökünü verir.
print("5. tanımı ve örneği")
sayi8= int(49) # Ana Sayı  
sayi8 **=0.5 # Kok aldıgımız sayı
print(sayi8)


### Dokunma
print("")
### Dokunma

# sayı **=(1/3) Sayının küpkökünü verir.
print("6. tanımı ve örneği")
sayi9= int(8) # Ana Sayı  
sayi9 **=(1/3) # Sayının küpkökünü verir.
print(sayi9)


### Dokunma
print("")
### Dokunma


# \' => Kaçış dizisi yani bu metnin bitişi olan tırnak işareti olmadığını belirtir.
print("7. tanımı ve örneği")
print('İzmir\'in boyozu meşhurdur.') # Tek Tırnakta oluyor 


### Dokunma
print("")
### Dokunma


# a[4:10] => 3.index 13.index kadar olan değerleri tanımlar.(4. ve 10.dahil değil!) [index=Harf]
print("8. tanımı ve örneği")
a = "programlamacılar"
print(a[3:13])

### Dokunma
print("")
### Dokunma


# a[:7] => Kelimenin başındaki değerden itibaren 10.değere kadar olan indeksleri tanımlar.(10.dahil değil!)
print("9. tanımı ve örneği")
a = "programlamacılar"
print(a[:7])


### Dokunma
print("")
### Dokunma


# a[:] => Kelimenin tamamının çıktısını alır.
print("10. tanımı ve örneği")
a = "programlamacılar"
print(a[:])


### Dokunma
print("")
### Dokunma


# a[:-1] => Kelimenin sondan 1 harfini eksilterek çıktı alır.
print("11. tanımı ve örneği")
a = "programlamacılar"    #programcıla olarak gösterir
print(a[:-1])


### Dokunma
print("")
### Dokunma


# a[::2] => Kelimeyi 2 harf 2 harf atlayarak çıktı alır. 
print("12. tanımı ve örneği")           
a = "programlamacılar" 
print(a[::3])


### Dokunma
print("")
### Dokunma


# a[::-1] => Kelimeyi tersten yazarak çıktı alır.
print("13. tanımı ve örneği") 
a = "programlamacılar"  
print(a[::-1])  

### Dokunma
print("")
### Dokunma


# Yapım Aşaması [ Başlama index : Bitiş index : Atlama index  ] #index=harf
print("14. tanımı ve örneği") 
a = "programlamacılar"  
print(a[1:3:5])  

### Dokunma
print("")
### Dokunma



#len(string) => Atanan değerin metinsel uzunluğunu belirtir(kaç harf)
print("15. tanımı ve örneği") 
deger= len ("programlamacılar bu işi yapıyor")  
print(deger)




### Dokunma
print("")
### Dokunma




#Not : String ifadedeki değerler değiştirilemez fakat önceki değer silinip yeni değer atanabilir. Örnek ;
print("16. tanımı ve örneği") 
a = "Bünyamin " 
b = "Ali "
c = "Tolga"
a = a + b + c + " Berkay"
print(a)


### Dokunma
print("")
### Dokunma




# \n => Verilen değişkeni alt satıra yazdırır.
print("17. tanımı ve örneği") 
print("Merhaba\nNasılsın\nİyi misin")



### Dokunma
print("")
### Dokunma



# \t => Verilen değişkenler arasında tab kadar(4 boşluk)boşluk verir.
print("18. tanımı ve örneği") 
print("Ocak\tMart\tŞubat")


### Dokunma
print("")
### Dokunma



# sep => Verilen değişkenlerin arasına atanılan değişkeni getirir.
print("19. tanımı ve örneği") 
print(35,43,54,65,sep = "/")


### Dokunma
print("")
### Dokunma



# * => Kelimedeki her bir harfi ayırarak yazar.
print("20. tanımı ve örneği") 
print(*"Python")


### Dokunma
print("")
### Dokunma



# Her harflerın arasına belırlenen değişkenı atar
print("21. tanımı ve örneği") 
print(*"Python", sep = "\ " )




### Dokunma
print("")
### Dokunma



# Her harflerın arasına belırlenen değişkenı atar
print("22. tanımı ve örneği") 
print(*"TBMM",sep =".")



### Dokunma
print("")
### Dokunma



# .format => Bazı yerlerde bir stringin içine daha önceden tanımlı string,float,int vs. değerleri yerleştirmek için kullanılır.
print("23. tanımı ve örneği") 
a = 13
b = 4
print("{} + {}'nin toplamı {}'dir".format(a,b,a+b))


### Dokunma
print("")
### Dokunma










