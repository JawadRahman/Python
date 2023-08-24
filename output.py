name="Jawad"
age=25
sal=20000

#Approch1
print(name,age,sal)

#Approch2
print("Name is: ",name)
print("Age is: ",age)
print("Sal is: ",sal)

#Approch3 :using % operator is imp
print("Name:%s Age:%d Salary:%g"%(name,age,sal))

#Approch4 : using {} value and operator is imp
print("Name:{} Age:{} Salary:{}".format(name,age,sal))

#Approch5
print("Name:{0} Age:{1} Salary:{2}".format(name,age,sal))
print("Name:{2} Age:{1} Salary:{0}".format(name,age,sal))
print("Name:{0} Age:{0} Salary:{2}".format(name,age,sal))