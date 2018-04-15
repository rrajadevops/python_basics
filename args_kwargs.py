# *args : will act as a tupple
# **kwargs will act as a set

def my_method(*args, **kwargs):
    print(args)
    print (kwargs)

my_method(3, 4, 5)

#out put will be
#(3, 4, 5)
#{}

my_method(3, 4, 5, name='Raja', age=27)
#output will be
#(3, 4, 5)
#{'name': 'Raja', 'age': 27}

