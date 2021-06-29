#list  is mutable
#list is similar to array in js     

fruits=["apple",'bannan','orange']
print(fruits)
print(type(fruits))
print(fruits[1])

for f in fruits:
    print(f)

if "kiwi" in fruits:
    print("yes its there")
else:
    print("its not there") 

print(len(fruits))
fruits.append("kiwi")
print(fruits)
print(len(fruits))

fruits.insert(1,"mango")
print(fruits)

fruits[2]="grapes"#update/replace
print(fruits)

fruits.remove("grapes")
print(fruits)

fruits.pop()
print(fruits)

del fruits[0]
print(fruits)


l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)

lst1=[1,2,3]
lst2=['abc','bda']
lst3=lst1+lst2
print(lst3)
lst1.extend(lst2)
print(lst1)



scores=[2,5,7,89,34]

print(scores)
print(scores[3])
print(scores[-3])
print(scores[2:4])
print(scores[0:2])
print(scores[3:])
print(scores[:3])
print(scores[1:5:2])