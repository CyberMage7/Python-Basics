# Greatest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if(a>b):
    if(a>c):
        print(a, "is greatest among", b, "&", c)
    else:
        print(c, "is greatest among", a, "&", c)
else:
    if(b>c): 
        print(b, "is greatest among", a, "&", c)
    else:
        print(c, "is greatest among", b, "&", a)