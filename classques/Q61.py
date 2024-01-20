#for returning count and printing n+1 perfect squares
#n=4 then output:1,4,9,16 and count=5(0 included)
'''def count_square(n):
    if(n>1):
        count=1#0 is a perfect square
        for i in range(1,n+1):
            sq=i**2
            print(sq)
            if((int(sq/i))==i):
                count+=1
        return(count)
    else:
        return(-1)'''

#for returning count and  printing of perfectsq <=n
def count_square(n):
    if(n>1):
        count=1#0 is a perfect square
        sq=0
        print(sq)
        i=1
        while(sq<n):
            sq=i**2
            print(sq)
            if(int(sq/i)==i):
                count+=1
            i+=1    
        return(count)
    else:
        return(-1)
    
#for checking the function
n=int(input("Enter value greater than 1 upto which you want the count of perfect squares:")) 
print("Count of perfect squares:",count_square(n))
