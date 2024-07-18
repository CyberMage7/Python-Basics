with open("problem.txt", "r") as f:
     data = f.read()
     x = data.replace("Java", "Python")

with open("problem.txt", "w") as f:
     f.write(x)