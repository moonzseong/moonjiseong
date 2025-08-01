array = []

temp = input().split()

for i in range (3):
    array.append(int(temp[i]))

A=array[0]
B=array[1]
C=array[2]

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
