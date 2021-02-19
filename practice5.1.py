a = ['dfgdfgdfg','dfgdfgdfg','sdfgdfgdfg']
def operations(a,operation):
    return operation(a)
def upper(a):
    res = list(map(str.upper,a))
    return res
def lower(a):
    res = list(map(str.lower,a))
    return res
print (operations(a,upper))
print (operations(a,lower))