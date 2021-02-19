f =open("pai.txt","r")
text = f.read()
from collections import Counter
print(Counter([''.join(filter(str.isalpha, x.lower())) for x in text.split() if ''.join(filter(str.isalpha, x.lower()))]))
#позаимствовал большую часть из интернета,зато понял, как работает)


