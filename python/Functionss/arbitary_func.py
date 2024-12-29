
# Arbitary function is function that take any number of arguments

def name(*args):
    print(args)
    print(type(args))
    for i in args:
        print(i)
        print(type(i))

name(1,2,3,4,5,6,7,8,9,10)


# Arbitary keyword function is function that take any number of keyword arguments

def name(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for i in kwargs:
        print(i)
        print(type(i))

name(name="ajith",age=34)
