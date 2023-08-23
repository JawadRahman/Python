print(10+10)    #valid
print(10.5+5.5) #valid
print("welcome"+"python")   #valid

print(10+10.5)  #valid
print(True+5)   #valid
print(False+5)  #valid
print(True+True)    #valid

#####invalid

print(10+"Python")      #TypeError
print(10.5+"Python")    #TypeError
print(True,"Python")    TypeError