a=15
if a>25:
    print("This condition is True")
else:
    print("This conditon is False")

#################################
if 1:
    print("True conditon")
else:
    print("False condtion")

####################################
if False:
    print("True conditon")
else:
    print("False condtion")

#Even or odd

a=15
if a%2==0:
    print("Even numbers")
else:
    print("odd number")

#Multiple Statement

print("Jawad") if True else print("Rahman")
print("Jawad") if False else print("Rahman")

print("10") if 10>20 else print("20")
print("10") if 10<20 else print("20")

{print("Good"),print("Morning")} if True else { print("Good"),print("Night")}
{print("Good"),print("Morning")} if False else {print("Good"),print("Night")}


#elif

a= 50

if a==10:
    print("Ten")
elif a==20:
    print("Tewenty")
elif a==50:
    print("Fifty")
else:
  print("not listed")