a=[1,2,3]
b=[3,4,5]
m=[[1 for col in range(4)] for row in range(4)]
m[1]=a
m[2]=b
print(m)