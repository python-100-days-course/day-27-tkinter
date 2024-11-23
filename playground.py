# 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
# Day 27 - Intermediate - Tkinter, *args, **kwargs and Creating GUI Programs

# Challenge:
    # Modify the add function to take an unlimited number of arguments.
    # Use a loop to sum all the arguments inside the function.
    # Test it out
print("\n*args: Many Positional Arguments")
def add(*args):
    print(f"args = {args}")
    print(f"args[0] = {args[0]}")
    print(f"args type is {type(args)}")
    answer = 0
    for n in args:
        answer += n
    return answer

print(add(1, 3, 5, 7))

print("\n**kwargs: Many Keyword Arguments")
def calculate(n, **kwargs):
    print(f"kwargs = {kwargs}")
    print(f"kwargs type is {type(kwargs)}")
    for key, value in kwargs.items():
        print(f"key = {key}")
        print(f"value = {value}")
    print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(f"n = {n}")

calculate(2, add=3, multiply=5)

# Example of **kw used in class object, which is similar to what Tkinter does
# For class Car make and model are required
# For class Car2 make and model are optional due to .get()
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

class Car2:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
my_car2 = Car2(make="Toyota")
print(f"my_car.model = {my_car.model}")
print(f"my_car2.model = {my_car2.model}")