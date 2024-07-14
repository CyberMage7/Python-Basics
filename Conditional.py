marks = float(input("Enter your marks: "))

if(marks>=90):
    print("Congratulations!!!")
    print("You secured A grade")
elif(marks>=80 and marks<90):
    print("Very Good!!")
    print("You secured B grade")
elif(marks>=70 and marks<80):
    print("Good!")
    print("You secured C grade")
else:
    print("You have to work hard")
    print("You secured D grade")