a = {"P.O":(1,2,9), "G.P":(10,7,8), "I.A":(7,12,10), "E.A":(10,12,11)}
m =(list(a.values()))
keys = (a.keys())
d = []
for values in m:
  values = [float(sum(values)) / len(values)]
  for i in values:
        d.append(i)
c =(dict(zip(keys,d)))
print (max(c,key=c.get))
print (min(c,key=c.get))
