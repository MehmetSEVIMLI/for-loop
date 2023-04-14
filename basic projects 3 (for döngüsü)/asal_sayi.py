# Girilen sayıın asal olup olmadığını bulan programı yaznız.
# Asal ise "EVET" değilse "HAYIR" yazacak.

# sadece kednisine ve 1 sayısına tam olarak bölünen sayılara asal denir.


n=int(input("Sayı giriniz: "))

sayi=0

for i in range(2,n):
    if n%i==0:
        sayi=sayi+1
        break
if sayi==0:
    print("EVET")
else:
    print("HAYIR")