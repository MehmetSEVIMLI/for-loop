# Girilen sayının gölenlerii bulan programı yazınız. 1 sayısı veya sayının kendisi dahil edilecek. 

sayi=int(input("sayı giriniz: "))

bolenler=[]

for i in range(1,sayi+1):
    if sayi%i==0:
        bolenler.append(i)
print(bolenler)