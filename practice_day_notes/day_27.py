# tkinter module introduction
# tk se derived h ye module
# tk k commands lekar k idhar kwargs m convert kardiya

#*args is used for unlimited positional arguments
#prints in tuple
def add (*args):
    print(args[1])
    sum = 0
    for n in args:
        sum += n
    return sum

#print(add(1,3,8,9))
#------------------
#**kwargs is used for unlimited keyword arguments
#prints in dictionary
def calculate(n,**kwargs):
    print(kwargs)
    n += kwargs["add"]
    n += kwargs["multiply"]
    print(n)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])-->3

calculate(8,add=3,multiply=4)
class Car:
    def __init__(self,**kw):
        # self.make = kw.get("make")-->if keyword isn't specifies then it won't
        #give an error instead print none
        #for reference refer fxn --> mycar.speed
        self.make = kw["make"]
        self.model = kw["model"]
        self.speed = kw.get("speed")
mycar = Car(make="Ford" , model="Mustang GT")
print(f"{mycar.make}'s {mycar.model} with a speed of {mycar.speed}")