def method1(another):
    return another()

def add():
    return 5 + 5

#print (method1(add))

#print (method1(lambda: 5 + 10))

my_list = [5, 10, 15, 20, 30]
print (list(filter(lambda x: x!= 15, my_list)))
print ([x for x in my_list if x != 15])

def not_fifteen(x):
    return x!= 10

print (list(filter(not_fifteen(), my_list)))

