#create string

#approch1
"""""
name="Welcome"
print(name)

#approch2
name1=str("Home")
print(name1)


#mutable

str1="welcome"
str2="welcome"

print(id(str1))      #1949903704304
print(id(str2))      #1949903704304

str2=str2+"to python"
print(id(str1))     #1949903704304
print(id(str2))     #1621495149264

#string operation + *

str="welcome "
print(str+"to programming")
print(str * 10)


#slicing string

str="Bangladesh"
print(str[2:5])
print(str[:5])
print(str[5:])

#ord() and chr()

print(ord('A')) #65
print(chr(65))  #A


str="england"
print(len(str))
print(max(str))
print(min(str))

#in and not in operator

str ="Python"
print("yth"in str) #true
print("abx" in str) #false
print("abx" not in str) #true


#string comparison

print("tim" == "tie")       #false
print("free" != "freedom")  #true
print("arrow">"aron")       #true
print("right">="left")      #true
print("teeth"<"tee")        #false
print("yellow"<="fellow")   #false
print("abc">"")             #true



s="python"
for i in s:
    print(s)

#Testing strings

s="welcome to pyrthon"

print(s.isalnum()) #false
print("welcome".isalpha())  #true
print("2022".isdigit())     #true
print("first number".isidentifier())        #false
print("WELCOME".isupper())  #ture
print(" ".isspace())        #true

"""""
#converting string

s ="String in PYTHON"
s1=s.capitalize()
print(s1)

s2=s.title()
print(s2)

s3=s.lower()
print(s3)

s4=s.swapcase()
print(s4)

s5=s.upper()
print(s5)

s6=s.replace("in","on")
print(s6)

print(s)
