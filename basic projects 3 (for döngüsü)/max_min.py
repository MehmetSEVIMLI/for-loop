# girilen "n" sayıdan maksimum ve minimum sayıları bulan programı yazınız.

n = int(input())
mx = int(input())
mn = mx

for i in range(n-1):
    x = int(input())
    if x > mx :
        mx = x
    if x < mn:
        mn = x
print(mn,mx)