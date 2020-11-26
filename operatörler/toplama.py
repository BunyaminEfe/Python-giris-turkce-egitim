# int Sayı türünden değikenlerde kulanılır [[[[  Örnek 1+1=2 sonucu  ]]]]
# float  Ondalıklı sayıalrı hesaplamada kullanılır [[[[ Örneğin 1.2 + 1.2 = 2.4 işlem sonucu ]]]]
# string metinsel İfadelerde kullanılır 
# input Dışarıdan veri girişi yapmak istediğimiz zaman kullanılır
# .format => Bazı yerlerde bir stringin içine daha önceden tanımlı string,float,int vs. değerleri yerleştirmek için kullanılır.

print("Merhaba Ben Bejo :)")


# Ondalıklı toplama kodu

sayi1= input ('1.float türünden bir sayı giriniz. ')
sayi2= input ('2.float türünden bir sayı giriniz. ')
toplam=float(sayi1)+float(sayi2)
print("Toplam : {}".format (toplam))


###############################################


# Düz Toplama Kodu 

sayi3= input ('1.int türnden sayiyi gir: ')
sayi4= input ('2.int türünden sayiyi gir: ')
toplam=int(sayi3)+int(sayi4)
print("Toplam : {}".format (toplam))


###############################################

# Basit Seviye İlk Toplama işlemi

sayi5=10
sayi6=20
toplam=int(sayi5)+int(sayi6)
print(toplam)