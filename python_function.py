###########################################################################
#
#   Fonksiyon Oluşturmak İçin 
#   Def Komutu Oluşturulur
#
###########################################################################

print("")
print("")
print("Bejo Kod Yazıyor.")
print("")
print("")

###########################################################################

print("1. Tanım Ve Örneği")
def benim_fonksiyonum(): # : iki nokta koyuluyor Önemli 
    print("İlk Fonksiyonumuz")

benim_fonksiyonum() # Print Komutunu Burada Algılar

###########################################################################
print("")
print("")
###########################################################################

###########################################################################
#
#   Argümanlar
#   Bilgi, işlevlere bağımsız değişken olarak aktarılabilir.
#   Bağımsız değişkenler, işlev adından sonra parantez içinde belirtilir. 
#   İstediğiniz kadar argüman ekleyebilirsiniz, sadece virgülle ayırmanız önemli.
#   Aşağıdaki örnekte tek bağımsız değişkenli 
#   işlev vardır. 
#   [2. Tanım da olan efe kelimesini istediğiniz bir şey yapababilrsiniz bir]
#   İşlev çağrıldığında, işlevin içinde tam adı yazdırmak için kullanılan bir ad iletiriz.
#
###########################################################################

print("2. Tanım Ve Örneği")
def fonksiyon_bilgiler(efe):
    print(efe + " Bilgileri")

fonksiyon_bilgiler("Telefon")
fonksiyon_bilgiler("Adres")
fonksiyon_bilgiler("Kişisel")

###########################################################################
print("")
print("")
###########################################################################

###########################################################################
#
#  Bağımsız Değişkenler
#  Varsayılan olarak belirtilen bir işlev doğru sayıda 
#  bağımsız değişkenle çağrılmalıdır. 
#  Yani, işleviniz 2 bağımsız değişken bekliyorsa, 
#  işlevi 2 bağımsız değişkenle çağırmanız gerekir, 
#  daha fazla değil, daha az değil.
#
###########################################################################

print("3. Tanım Ve Örneği")
def bagımsız_fonksiyon(Bünyamin, Efe):
    print(Bünyamin + " " + Efe)

bagımsız_fonksiyon("Araba", "Sürüyor")

###########################################################################
print("")
print("")
###########################################################################

###########################################################################
#
#  Hadi Az Eylenceli ŞEyler Yapalım
#  Fonksiyonunuza kaç argüman aktarılacağını 
#  bilmiyorsanız * fonksiyon tanımında parametre adından bir önce ekleyin.
#  Bu şekilde işlev alacak başlığın argümanlarından ve buna göre bütün öğelere erişebilir
#
###########################################################################

print("4. Tanım Ve Örneği")

def keyifli_argümanlar(*öğrenciler): # * önemli
    print("Sınıftaki Öğrenci " + öğrenciler[2])

keyifli_argümanlar("Ali", "Berkay", "Bünyamin")

###########################################################################
print("")
print("")
###########################################################################

###########################################################################
#
#  Anahtar Kelime ve Bağımsız Değişkenleri
#  Anahtar= değer sözdizimi ile bağımsız değişkenler de gönderebilirsiniz.
#  Bu şekilde argümanların sırası önemli olmaz.
#
###########################################################################

print("5. Tanım Ve Örneği")

def bagımsız_değişkenler(öğrenci1, öğrenci2, öğrenci3):
    print("Üniversite Öğrencisi " + öğrenci3)

bagımsız_değişkenler(öğrenci1 = "Ali",  öğrenci2 = "Berkay", öğrenci3 = "Bünyamin") 

###########################################################################
print("")
print("")
###########################################################################

###########################################################################
#
#  İşlevinize kaç anahtar kelime ve bağımsız değişkeni geçirileceğini 
#  bilmiyorsanız ** kullanılır. 
#  İşlev tanımında parametre adından önce iki yıldız işareti ekleyin.
#  Bu şekilde işlev bir argüman sözlüğü alacak ve öğelere uygun şekilde erişebilir.
#
###########################################################################

print("6. Tanım Ve Örneği")
def iki_yıldız(**ismi):
  print("Kişinin soyadı " + ismi["Soyadı"])

iki_yıldız(Kendiismi = "Bünyamin", Soyadı = "Efe")

###########################################################################
print("")
print("")
###########################################################################

###########################################################################
#
#  Varsayılan Parametre Değeri
#  Aşağıdaki örnek 
#  Varsayılan bir parametre değerinin nasıl kullanılacağını gösterir.
#  Fonksiyonu bağımsız değişken olmadan çağırırsak, varsayılan değeri kullanır.
#
###########################################################################

print("7. Tanım Ve Örneği")
def ülke_isimleri(ülke = "Türkiye"):
    print("O ülkenin adı " + ülke)

ülke_isimleri() # burdaki boş değer Ülkeye Belirlediğimiz Değeri Alacak
ülke_isimleri("Azerbeycan")
ülke_isimleri("Kazakistan")
ülke_isimleri("Kıbrıs")

###########################################################################
print("")
print("")
###########################################################################
###########################################################################
#
#  Dönen Değerler
#  Bir işlevin bir değer döndürmesine izin 
#  vermek için şu return ifadeyi kullanın
###########################################################################

print("8. Tanım Ve Örneği")
def çarpma_fonksiyon(x):
    return 5 * x
print(çarpma_fonksiyon(3))
print(çarpma_fonksiyon(10))
print(çarpma_fonksiyon(5))
 
###########################################################################
print("")
print("")
###########################################################################
###########################################################################
#
#  Geçiş Bildirimi
#  functiontanımlar boş olamaz, 
#  ancak herhangi bir nedenle functioniçeriği olmayan bir tanımınız varsa
#  passhata almamak için ifadeyi ekleyin.
#
###########################################################################

print("9. Tanım Ve Örneği")
print("Kodu İncele")
def bos_fonksiyon():
  pass
# bunun gibi boş bir işlev tanımına sahip olmak, pass deyimi olmadan bir hataya neden olur

###########################################################################
print("")
print("")
###########################################################################
###########################################################################
#
#  Özyineleme
#  Python ayrıca işlev özyinelemesini de kabul eder, bu da tanımlanmış bir işlevin kendisini çağırabileceği anlamına gelir.
#
#  Özyineleme, yaygın bir matematiksel ve programlama kavramıdır. Bir işlevin kendisini çağırdığı anlamına gelir. 
#
#  Bu, bir sonuca ulaşmak için veriler arasında döngü yapabileceğiniz anlamına gelir.
#  Geliştiricinin özyineleme konusunda çok dikkatli olması gerekir 
#  çünkü hiçbir zaman sona ermeyen veya fazla miktarda bellek veya 
#  işlemci gücü kullanan bir işlevi yazmak oldukça kolay olabilir. 
#  Bununla birlikte, doğru yazıldığında yineleme, programlama için çok verimli ve 
#  matematiksel açıdan zarif bir yaklaşım olabilir.
#
#  Aşağıdaki Örnekte, tri_recursion () , kendisini çağırmak ("recurse") için tanımladığımız bir işlevdir. 
#  Kullandığımız k azaltır (veri olarak değişken -1 ) her sefer Recurse.
#  Yineleme, koşul 0'dan büyük olmadığında (yani 0 olduğunda) sona erer.
#
#  Yeni bir geliştirici için bunun tam olarak nasıl çalıştığını anlamak biraz zaman alabilir, 
#  öğrenmenin en iyi yolu onu test etmek ve değiştirmektir.
###########################################################################

print("10. Tanım Ve Örneği")
def tri_recursion(A):
    if (A > 0):
        result = A + tri_recursion(A - 1)
        print(result)
    else:
        result = 0
    return result
print("Özyineleme Örneği Sonuçları")
tri_recursion(6)

###########################################################################
print("")
print("")
###########################################################################




