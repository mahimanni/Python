from os import read
f=open('myfile.txt','r')
f.seek(10)
data=read(5)
print(data)
