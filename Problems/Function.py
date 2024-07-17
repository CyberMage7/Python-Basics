# nums = [1,2,3,4,5,6,7,8,9,10]

# def print_list(list):
#     for i in list:
#         print(i, end=" ")

# print_list(nums)

n = int(input("Enter the number to be checked: "))

def check(m):
    if(m%2==0):
        return "EVEN"
    else:
        return "ODD"
    
print(check(n))