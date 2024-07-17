# n = int(input("Enter the number n: "))

# def func1(m):
#     if m==1:
#         return 1;
#     return m+func1(m-1)

# print(func1(n))

string = ["JOLLY LLB2", "Housefull 4", "De Dana Dan"]

def func2(list, i):
    if(i==len(list)): return 
    print(list[i], end=" ")
    func2(list, i+1)

func2(string, 0)