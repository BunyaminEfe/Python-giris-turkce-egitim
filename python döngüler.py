###########################################################################
#
#
# Python Döngüleri
# Python'da iki ilkel döngü komutu vardır
# Döngüler sırasında
# İçin döngüler
# 
#
###########################################################################

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

# 6 tan küçğk tüm rakamları yazar
print("1. Tanım Ve Örneği")
bejo = 1
while bejo < 6: # Buradaki tüm rakamı değitirilecek iki nokta öenmli koy
  print(bejo)
  bejo += 1

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

print("2. Tanım ve Örneği")
bejo = 1
while bejo < 6: # Burdaki iki nokta önemli
   print(bejo)
   if bejo == 3: # iki nokrayı unutma
     break
   bejo += 1

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

print("3. Tanım ve Örneği")
efe = 1
while efe < 6:
    print(efe)
    efe += 1
else:
    print("o şahıs 6 dan küçük değil")

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################

print("4. Tanım ve Örneği")
bejo = 0
while bejo < 6:
  bejo += 1
  if bejo == 3: # 3 rakamını atlar ve yada belirtilen kodu geçer
    continue # dongü bir sonraki adıma geçer 
  print(bejo)

#####################------------------------------########################
print("")
print("")
#####################------------------------------########################











