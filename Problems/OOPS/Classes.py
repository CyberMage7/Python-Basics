# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def calc_avg(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#         print("Average of", self.name, "is", sum/3)

#     @staticmethod
#     def greet():
#         print("Hello")

# s1 = Student("Shagun", [76, 78, 89])
# s1.greet()
# s1.calc_avg()


class Account:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
         self.balance-=amount
    
    def credit(self, amount):
         self.balance += amount
    def print_bal(self):
        print("Current Balance: ", self.balance)
    
a1 = Account(1000, 456789)
a1.print_bal()

a1.debit(500)
a1.print_bal()

a1.credit(800)
a1.print_bal()
a1.debit(200)
a1.print_bal()
