d = [1, 23, 45, 67, 2334, 89, 5, 3, 6]
l = []
k = 0
for i in d:
    for h in range(2, i):
        if i % h == 0:
            k = k + 1
    if k == 0:
     l.append(i)
    else:
      k = 0
def square(u):
    return u*u
squares = list(map(square,l))
print (squares)