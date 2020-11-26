###########################################################################
#
# Dosya işleme, herhangi bir web uygulamasının önemli bir parçasıdır.
# Python, dosyaları oluşturmak, okumak, güncellemek ve silmek için çeşitli işlevlere sahiptir.
# 
#                           Dosya yönetimi:
# Python'da dosyalarla çalışmak için anahtar işlev, open()işlevdir.
# open()İşlevi, iki parametre alır; dosya adı ve mod .
# Bir dosyayı açmak için dört farklı yöntem (mod) vardır:
#                           
#            "r"- Oku - Varsayılan değer. Okumak için bir dosya açar, dosya yoksa hata
#            "a" - Ekle - Eklemek için bir dosya açar, mevcut değilse dosyayı oluşturur
#            "w" - Yaz - Yazmak için bir dosya açar, yoksa dosyayı oluşturur
#            "x" - Oluştur - Belirtilen dosyayı oluşturur, dosya varsa bir hata döndürür
#                           
# Ek olarak, dosyanın ikili mod mu yoksa metin modu olarak mı işleneceğini belirtebilirsiniz
#            "t"- Metin - Varsayılan değer. Metin modu
#            "b" - İkili - İkili mod (örneğin görüntüler)                      
#
###########################################################################

print("")
print("")
print("Bejo Kod Yazıyor.")
print("")
print("")

###########################################################################

f = open("deneme.txt", "rt")




#####################------------------------------########################
print("")
print("")
#####################------------------------------########################