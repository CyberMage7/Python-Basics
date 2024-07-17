nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a = int(input("Enter the number to be searched: "))
for val in nums:
    if(a==val):
        print("Number found")
        break
    else:
        print("Searching...")
else:
    print("End of loop Number not found")