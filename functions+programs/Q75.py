#Generating 3 random integers b/w 100 to 999 which are divisible by 5
#importing random module
import random
l=[]

#effective method
for i in range(3):
    l.append(random.randrange(100,1000,5))

#other method
'''count=0
while(count<3):
    a=random.randint(100,999)
    if(a%5==0):
        l.append(a)
        count+=1'''

print("Random integers b/w 100-999: ",l)    
