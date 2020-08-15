a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))
if a < b > c or a > b < c:
    print('middle', a)
elif b < a > c or b > a < c:
    print('middle',b)
elif c < a >b or c > a < b:
   print('middle',c)
elif a == b or b == c:
    print("False")




