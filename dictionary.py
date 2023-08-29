friends={'Jawad':'777-666-999',
        'Joy'  :'111-333-888'}

print(friends)  #{'Jawad': '777-666-999', 'Joy': '111-333-888'}


#Retriving element from the dictionary
print(friends['Joy'])   #111-333-888

#Adding element into the dictionary
friends['bob']='888-666-444'
print(friends)      #{'Jawad': '777-666-999', 'Joy': '111-333-888', 'bob': '888-666-444'}

#Modify element into the dictonary
friends['bob']='888-666-777'
print(friends['bob'])

#delecting element from the dictionary

del friends['bob']
print(friends)   #{'Jawad': '777-666-999', 'Joy': '111-333-888'}


#looping items in the dictionary

values = {
    'a' : '100',
    'b' : '200',
    'c' : '300',
    'd' : '400',
}
for i in values:
    print(i ,":",values[i])
    print(values)
    print(len(values))  #4


#Equlity Test

d1={"mike":41,'bob':35}
d2={"bob":35,'mike':41}

print(d1==d2)   #True
print(d1!=d2)   #False

#Dictionary methods

friends={'Jawad': '777-666-999', 'Joy': '111-333-888', 'bob': '888-666-444'}

#popitem
print(friends.popitem())
print(friends)

#clear()
print(friends.clear())
print(friends)

friends={'Jawad': '777-666-999', 'Joy': '111-333-888', 'bob': '888-666-444'}

#keys in tuple formet
print(friends.keys())       #dict_keys(['Jawad', 'Joy', 'bob'])
print(friends.values())     #dict_values(['777-666-999', '111-333-888', '888-666-444'])

print(friends.get('Joy'))  #111-333-888
print(friends.get('Jawad')) #777-666-999

print(friends)
print(friends.pop('Joy'))
print(friends)