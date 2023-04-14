# Girilen "n" sayısının faktorilyelini hesaplayan programı yazınız.

n=int(input("faktöriyleini almak istediğiniz sayı: "))
sonuc=1
for i in range(1,n+1):
    sonuc*=i
    
print("sonuç: ",sonuc)