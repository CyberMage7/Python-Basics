# r-> read the data
# w->overwrites the entire file
# a->adds to the file without harming the previous data 

f = open("demo.txt", 'r')
# data = f.read()
# print(data)

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

f.close()


# to delete a file:

# import os

# os.remove("filename.txt")