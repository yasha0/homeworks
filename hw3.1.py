my_file = open("123.txt", "r")
sum1 = []
for s in my_file:
    number = list(map(int, s.split()))
    fizz = number[0]
    buzz = number[1]
    c = number[2]
    for i in range(1 , c + 1):
        if i % fizz == 0 and i % buzz == 0:
            sum1.append("FB")
        elif i % fizz == 0:
            sum1.append("fizz")
        elif i % buzz == 0:
            sum1.append("buzz")
        if i % fizz and i % buzz:
            sum1.append(i)
print(sum1)
my_file.close()
