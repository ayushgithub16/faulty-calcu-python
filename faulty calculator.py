"""this is faulty calculator"""
a=int(input("enter first number you want to calculate   ANS:-"))
b=input("enter a sign you want to use     ANS:-")
c=int(input("enter second number you want to calculate   ANS:-"))

if a==45 and b=="*" and c==3:
    print(a,b,c,"=",555)
elif a==56 and b=="+" and c==9:
    print(a,b,c,"=",77)
elif a==56 and b=="/" and c==6:
    print(a,b,c,"=",(4))
elif b=="*":
    print(a,b,c,"=",a*c)
elif b=="+":
    print(a,b,c,"=",a+c)
elif b=="/":
    print(a,b,c,"=",a/c)
elif b=="-":
    print(a,b,c,"=",a-c)