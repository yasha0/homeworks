fizz = int(input("print fizz "))
buzz = int(input("print buzz "))
a = int(input("print a number "))
b = list(range(1, a + 1))
my_list = []
for y in b:
    if y % fizz == 0 and y % buzz == 0:
        my_list.append("FB")
    elif y % fizz == 0:
        my_list.append("F")
    elif y % buzz == 0:
        my_list.append("B")
    if y % fizz and y % buzz:
        my_list.append(y)
print(list(my_list))