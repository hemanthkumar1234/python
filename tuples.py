#tuples are immutable
fruits=("apple","banana","orange")


print(fruits)
print(type(fruits))


#fruits[1]="grapes" #error
print(fruits[1])
print(fruits[-2])
print(fruits[2:4])


t1=("apple",)
print(t1)
print(type(t1))


for f in fruits :
    print(f)

if "kiwi" in  fruits:
    print("yes its there")
else:
    print("its not there")

del fruits
#print(fruits)#error


t1=(1,2,3)
t2=(4,5,6)


t3=t1+t2
print(t3)

print(t3.count(2))
