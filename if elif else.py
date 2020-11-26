###########################################################################
#
# Python Koşulları ve If ifadeleri
# Python Matematik ve olağan dışı mantıksal koşulları destekler
#
#                           Önemli Değerler:
#
#                           Eşittir: a == b
#                           Eşit Değil: a! = B
#                           Küçüktür veya eşittir: a <= b
#                           Şundan büyük: a> b
#                           Büyük veya eşit: a> = b
#                           
# Bu koşullar en yaygın if ifadelerinde  kullanılır. 
# Dögülerdede olmak üzere değişik şekillerde kullanılır.
# if anlamı "eğer" kelimesi anlamına gelir.                            
#
###########################################################################

print("")
print("")
print("Bejo Kod Yazıyor.")
print("")
print("")

###########################################################################
#
# if elif else Bu Günkü Öncelikli kelimelerimiz :)
#
###########################################################################

# Burada klasik matematikte bildiğimiz küçüktür büyüktür ifadelerini kullnıyoruz 2>1 den gibi
print("1. Örnek ve Tanımı")
a = 33
b = 200
if b > a:
    print("b sayısı a sayısından büyük")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

###########################################################################
#
# Elif anahtar kelime doğru değil ise 2. anahtar kelimeyi gösterir
#
###########################################################################

# Bu Örnekte a sayısı b sayısına eşittir. 
# Bu yuzden elif koşulu ile a saysii b sayısan eşittir yazısını yazdırabildik.
print("2. Örnek ve Tanımı")
a = 10
b = 10
if b > a: 
    print("b sayısı a sayısından büyüktür")
elif a==b:
    print("a sayısı ile b sayısı birbirine eşittir")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

###########################################################################
#
# else önceki oluşmuş koşullara göre olumsuzsa sonuç olarak gösterir.
#
###########################################################################

# üstteki sonuçlar olumsuz geldiği için else komudu döndü
print("3. Tanım Ve Örneği")
a = 120
b = 60
if b > a: # 2 nokta koymayı unutma önemli
    print ("B sayısı A sayısından büyüktür")
elif a==b: # 2 nokta koymayı unutma önemli 
    print("A sayısı ile B sayısı biribirine eşit değerlerdir.")
else:
    print("A sayısı B sayısından büyüktür")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# İlk deperimiz olumsuzoldugu için 2. değeri kullanmaya başladık.
print("4. Tanım ve Örneği")
a = 250
b = 100
if b > a:
    print("B büyüktür A sayısından")
else:
    print("B sayısı A sayısından büyük değildir")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# if a > b: sonra print yazıp kod ekleyebılyıoruz kısa yoldan
print("5. Tanım ve Örneği")
a = 250
b = 100
if a > b: print("A sayısı B sayısından büyüktür")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# Hangi Değer büyükse o değeri yazar
# Else kısa tarzda kod yazma örneği
print("6. Tanım ve Örneği")
a = 10
b = 68
print("A büyüktür") if a > b else print("B büyüktür") 

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

###########################################################################
#
# Bu teknik, Üçlü Operatörler veya Koşullu İfadeler olarak bilinir .
#
###########################################################################

# 3 koşullu bir ifade if else else kısa hali
print ("7. Tanım ve Örneği")
a = 321
b = 321
print("A sayısı büyüktür") if a > b else print("= eşittir") if a==b else print("B sayısı büyüktür")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

###########################################################################
#
# and mantıksal bir operatordur ve koşullu ifadeleride birleştirmek için kullanılır
#
###########################################################################

# verdiğigimiz 3 sayıyı kendi aralarıdna buyuktur küçüktür yaptırmiş olduk
print("8. Tanım Ve Örneği")
a = 100
b = 50
c = 200
if a > b and c > a:
    print ("Her iki koşulda doğrudur.")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

###########################################################################
#
# or mantıksal bir operatordur ve koşullu ifadeleride birleştirmek için kullanılır
#
###########################################################################

# or sayesıdne tek ifadenin doğru olması bize sonucu olumlu göstermesine yaradı
print("9. Tanım ve Örneği")
a = 100
b = 50 
c = 200
if a > b or a > c:
    print("Koşullardan biri doğrudur") # a sayısı b sayısından büyüktür

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# if İfadelerin içinde if ifadeleriniz olabilir , buna iç içe if ifadeler denir .
print("10. Tanım ve Örneği")
x = 89
if x > 10:
    print("89 sayısı 10sayısından büyüktür.")
    if x > 20:
        print("89 sayısı 20 sayısıdan büyüktür")
    else:
        print("89 sayısı 20 sayısının buyuk bir sayıdır")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# herhangibir hata mesaji almamak için pass terimi kullanılır
print("11. Tanım ve örneği")
a = 33
b = 200
if b > a:
    pass # Hata Mesajlarını engeller.
print("Hata Mesajı yok")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################