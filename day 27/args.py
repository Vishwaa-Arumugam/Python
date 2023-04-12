# def fun(*args):
#     a = 0
#     for i in args:
#         a += i
#     print(a)

# fun(4,5,6,7,8,9)

def calculate(**kwargs):
    print(kwargs)


calculate(add = 3, mul = 5)

def a(s,e,t = 'kjfgf',h =0):
    print(s,e,t,h)

a(1,2)

# class Car:

#     def __init__(self, **kwargs):
#         print(kwargs)
#         self.make = kwargs["make"]
#         self.model = kwargs["model"]
        

# my_car = Car(make = "bmw", model = 1)
# print(my_car.make, my_car.model)


