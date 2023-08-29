t1=()
t2=(11,26,33,46)
t3=([1,2,3,4,5,6])

t4=tuple("abc")
t5=tuple("Bangladesh")

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

t6=(1,5,6,7,8,10,25,15,17,19)

print(min(t6))
print(max(t6))
print(len(t6))
print(sum(t6))
#print()

for i in t6:
    print(i,end=" ")
####
print(t6[4:8])      #8,10,25,15
print(t6[:6])       #1,5,6,7,8,10
print(t6[6:])       #15,17,19

print(15 in t6)     #True
print(663 not in t6)    #True


