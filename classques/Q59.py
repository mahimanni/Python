def alternating(l):
    for i in range(len(l)):
        if(i%2==0):#1st pos even 
            if(l[i]%2==0):#and starting with even no
                pass
            else:
                return False
        else:
            if(l[i]%2!=0):#no are alternatively odd and even
                pass
            else:
                return False
    return True
#for checking the function
print(alternating([2,3,6,7]))
print(alternating([8,1,8,5]))
print(alternating([8,1,5,7]))
