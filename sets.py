fruits={"apple","banana","orange"}
print(fruits)
print(type(fruits))

for f in  fruits:
    print(f)

if "Apple" in fruits:
    print("yes its true")
else:
        print("its not there")
fruits.add("kiwi")
print(fruits)
#tuple, list, set
fruits.update(("kiwi","grapes"))
print(fruits)