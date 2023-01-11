#1
x = 10
y = x
if id(x) == id(y):
    print("x and y refer to the same object")

#2
x = 10
y = x
x += 1
if id(x) != id(y):
    print("x and y do not refer to the same object")    

#3
import gc
print(gc.get_threshold())

#4
import gc
print(gc.get_count())

#5
import gc
print(gc.collect())

#6
import gc
gc.get_threshold()
gc.set_threshold(7777, 11, 11)
print(gc.get_threshold())

#7
import sys, gc
def create_cycle():
    list = [8, 9, 10]
    list.append(list)
def main():
    print("Creating garbage...")
    for i in range(8):
        create_cycle()

    print("Collecting...")
    n = gc.collect()
    print("Number of unreachable objects collected by GC:", n)
    print("Uncollectable garbage:", gc.garbage)
if __name__ == "__main__":
    main()
    sys.exit()

#8
class Python:
 
    def __init__(self):
        print('The object is created.')
 
    def __del__(self):
        print('The object is destroyed.')
obj1 = Python()
obj2 = obj1
obj3 = obj1
print("Set obj1 to None")
obj1 = None
print("Set obj2 to None")
obj2 = None
print("Set obj3 to None")
obj3 = None

#9
import sys
str = "Welcome to Python"
print(sys.getrefcount(str))
 
arr = []
arr.append(str) # appending to an array
print(sys.getrefcount(str))
 
dict = {}
dict['str'] = str # adding to a dictionary
print(sys.getrefcount(str))
 
arr = [] # resetting the array
sys.getrefcount(str)
dict['my_str'] = "Some other string"
print(sys.getrefcount(str))