# '''
# file = open(r'C:\Users\munch\demo\myFile.txt','w')      #open file for writing
#
# file.write("This is my first name\n")
# file.write("This is my Last name\n")
#
# file.close()
# '''


# #reading all the data from file
#
# file = open(r"C:\Users\munch\demo\myFile.txt","r")
# print(file.read())
# print(file.readlines())
# print(file.readline())      #only the first line
# file.close()

#
f = open(r"C:\Users\munch\demo\myFile.txt","r")
# f.write("Welcome to python\n")
# f.write("Welcome to Java\n")
# f.write("Welcome to SQL\n")
# f.close()

for i in f:
    print(i)
f.close()









