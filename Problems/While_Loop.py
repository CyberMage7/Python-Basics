# n = int(input("Enter any number:"))
# i=1
# while i<=12:
#     print(n, "*", i, "=", n*i)
#     i+=1

sum=0
i=1
n=int(input("Enter the number n: "))
while i<=n:
    sum+=i
    i+=1
print("Sum of first n natural numbers is:", sum)