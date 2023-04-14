# "n" sayısı giriliyor ve daha sonra n sayı giriliyor. Girilen n sayının toplamını bulna progrmaı yazınız.
# sayıların ortalamasını bulan program yazınız.

n=int(input("Adet: "))
toplam=0

for i in range(5):
    sayi=int(input("sayilari giriniz: "))
    toplam=toplam+sayi
print("toplam: ",toplam)
print("ortlama: ",toplam/n)