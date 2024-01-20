def reverse(n,r):
    if(n>0):
        a=n%10
        return(reverse(n//10,a+(r*10)))
    else:
        return r

#for checking the reverse function    
n=int(input("Enter a number:"))
print("Reverse of a number is:",reverse(n,0))
