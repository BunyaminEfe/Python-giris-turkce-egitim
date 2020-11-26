#                           MANTIKSAL BAĞLAÇLAR
#Mnatıksal bağlaçlar 2 veya daha fazla karşılaştırma işlemini aynı koşulun içinde kontrol ediliyorsa;
#Bu bağlaçlara mantıksal bağlaçlar denir.

#NOT:Bu bölüme bakmadan önce mantıksal değerler ve karşılaştırma operatörlerine bakınız.

#NOT:İkiden fazla koşul kullanabiliriz.

#NOT:"<" ">" ifadelerini kullanırsak kelimeleri alfabeye göre sıralar örnek olarak araba < zürafa dersek 
# bunu true olarak algılar aklınızda bulunsun. 

# "and","or" ve "not" operatörü olacak şekilde üç tane operatör vardır.

############## and operatörü ##################
#"and" operatörünü kullandığımız zaman verilen koşulların hepsi doğruysa true, bir tanesi bile yanlışsa sonuç
#false olur.

print("1.örnek")
a = 1 < 2 and "murat" == "murat"
print(a) #Verdiğimiz iki koşulda doğru olduğu için true cevabını alıyoruz

print("")

print("2.örnek")
b = 2 < 1 and "elma" != "armut"
print(b) #Verdiğimiz koşullardan biri doğru diğeri yanlış olduğu için yanlış

print("")

############### or operatörü ##################
#"or" operatörünü kullandığımız zaman verilen koşulların 1 tanesi bile doğru olsa true,hepsi yanlışsa false olur.

print("3.örnek")
c = "araba" > "silah" or 55 != 65 
print(c) #Yazdığımız koşullardan bir tanesi doğru olduğu için true cevabını alırız.

print("")

print("4.örnek")
d = "patlıcan" == "emir"  or 45 > 87
print(d) #Yazdığımız iki koşulda yanlış olduğu için false cevabını alırız.

print("")

print("5.örnek")
e = 85 > 46 or "zafer" != "yenilgi" or "aslan" == "kaplan" 
print(e) #Sadece 1 tane doğru olması True cevabını almamız için yeterli.

print("")

############ not operatörü #############
#"not" operatörü aslında bir mantıksal bağlaç değildir.Bu operatörü bir mantıksal dğeri veya karşılaştırma
#işleşlemlerini tam tersine çevirir. True olan cevabı False yapar.False olan cevabı True yapar.

print("6.örnek")
f = "kivi" == "kivi" #Normalde kivi kiviye eşittir anlamı sağlıyor ve bu doğru .
print(not(f))       #Ama not operatörü eklediğimiz için cevap false oluyor.

print("")

print("7.örnek")
g = 35 > 37    
print(not(g))   #Cevap false olması gerekirken not operatörü yüzünden true oluyor

print("")

############### Mantıksal operatörleri beraber kullanmak #############

print("8.örnek")
h = not(35 > 27 or ("murat" == "mehmet")) 
print(h)  #Başında not olması cevabı true ama not olduğu için false oluyor.

print("")

print("9.örnek")
ı = not(58 < 69 or ("araba" != "silah" and 73 < 64))
print(ı) # 2. parantezli kısım  false sonrasında or kullanılan kısım true ama not olduğu için false cevabını aldık
