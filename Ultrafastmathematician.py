x = input()
lst1 = []
for i in range(0, len(x)):
    lst1.append(int(x[i]))

y = input()
lst2 = []
for i in range(0, len(y)):
    lst2.append(int(y[i]))

lst3 = []

for i in range(0, len(x)):
    if (int(lst1[i]) + int(lst2[i]) == 0):
        lst3.append(0)
    if (int(lst1[i]) + int(lst2[i]) == 1):
        lst3.append(1)
    if (int(lst1[i]) + int(lst2[i]) > 1):
        lst3.append(0)

b = ""
for i in lst3:
    b = b + str(i)
    
    
print(b)