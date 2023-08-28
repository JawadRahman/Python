#creating list
"""""
list1 =list()
print(list1)

list2=list([20,25,28,30])
print(list2)

list3=list(["Tom","And","Jerry"])
print(list3)

list4=list(["Welcome to Python"])
print(list4)

#acces in list

l=([1,2,3,4,5,6,7,8])
print(l[5])
print(l[0])
print(l[4])

#list operations

list6=[2,5,7,8,11,51,25,65,40,22,19]
print(6 not in list6) #True
print(2 in list6)   #true
print(len(list6))   #11
print(min(list6))
print(max(list6))
print(sum(list6))
print(list6[2:5])
print(list6[:10])
print(list6[10:])


# + & *
list7=[1,2,3]
list8=[8,9,10,100]
list9=list7+list8
print(list9)

print(list9 * 2)


#Travelling in list

list10=[1,2,3,4,5]

for i in list:
    print(i, end=" ")


"""""
"""""
list11 = [2,4,5,6,7,8,9]
list11.append(11)
list11.append(4)
print(list11)
print(list11.count(4))

list12 = [99,96,69]
list12.append(100)
list11.extend(list12)
print(list11)


print(list11.index(100))

list11.insert(1,100)
print(list11)

print(list11.pop(2))
print(list11)

list11.remove(100)
print(list11)

list11.reverse()
print(list11)


list11.sort()
print(list11)

"""""

#list comprehension

for x in range(10):
    print(x)

list13=[x for x in range(10)]
print(list13)

list13=[x+1 for x in range(10)]
print(list13)

list13=[x for x in range(10) if x%2==0]
print(list13)