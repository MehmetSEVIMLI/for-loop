## KULLANIM

# for i in range(5):
    # print(i)
    # çıktı: 0,1,2,3,4
    
## ÖRNEKLER


# for i in range(1,11): # başlangıç değerimiz ve bitiş değerimizi alır lakin son elemanı dagil etmez.
#     print(i)          # çıktı : 1,2,3,4,5,6,7,8,9,10
    
########  

# for i in range(1, 10, 2): # başlangıç - bitiş - artış değerleri 
#     print(i)              # çıktı: 1, 3, 5, 7, 9
    
#######

# for i in range(10,1,-2): #başlangıç - bitiş - azalış değeri
#     print(i)             # çıktı : 10, 8, 6, 4, 2
    
    
########

# n=int(input("bitiş değeri: "))
# toplam=0

# for i in range(1,n+1):
#     toplam=toplam+i
#     print(i)
# print(toplam)
    
########################################    
    
# for i in "kırmızı","turuncu","sarı","yeşil","mavi","lacivert","mor":
#     print(i)

################

# 0 gördüğünde dursun.

# for i in "kırmızı","turuncu","sarı","yeşil",0,"mavi","lacivert","mor":
#     if i==0:
#         break
#     print(i)
    
################

# 0 gördüğünde 0'ı yazmadan devam etsin

for i in "kırmızı","turuncu","sarı","yeşil",0,"mavi","lacivert","mor":
    if i==0:
        continue
    print(i)