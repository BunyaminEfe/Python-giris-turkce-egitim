print("Merhaba Ben Bejo :)")

print("")
# in x değerinin içindeki kelimeler arasında print komutundaki 1 kelimeyi aramasını sağlar.
# kelime x değerinin içinde varsa true yoksa false
print("1. tanımı ve örneği") 
x = ["acaba", "bejo", "efe", "asd", "123"]
print("bejo" in x) #kelime x değerinde var
print("sss" in x) #kelime x değerinde yok 

print("")
# not in x değerindeki kelimelerde print komutundaki kelime yoksa olumlu sonuç verir.
# eğer kelime x değerinde aranan kelime var ise olumsuz sonuç verir
print("2. tanımı ve örneği") 
x = ["kiraz", "çilek", "armut", "muz"]
print("karpuz" not in x) #Sunuç Olumlu
print("muz" not in x) # sonuç Olumsuz
