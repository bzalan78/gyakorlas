k=int(input("Ha egy szám négyzetét (1), vagy ha 2-szereséd szeretnéd(2) de ha semmi nem kell akkor (3). "))
s=1
d=2
h=3
if k==s:
    n=int(input("adj meg egy számot aminek a négyzetét kéred "))
    print(n*n)
elif k==d:
    l=int(input("adj meg egy számot aminek a kétszeresét írom ki "))
    print(l*2)
elif k==h:
    print("Viszlát")