def abc():
    print("hello")
abc()

def show(a,b):
    print('a=',a,'b=',b)

show(1,2)
show(b=1,a=2)


def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(add(1,2))
print(add(1,2,5,8))
print(add(1,2,9,8,7))
print(add(1,2,4,7,6))

#key value ->dict

def myf(**kwargs):
    print(kwargs["eid"],kwargs["ename"])

myf(eid=101,ename="hemanth")


def docdemo():
    """
    this is doc string
    """
    txt='''text in multiple lines'''
    print(txt)

docdemo()
print(docdemo.__doc__)


