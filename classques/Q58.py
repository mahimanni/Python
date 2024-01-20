def prime(start,end):
    print("Prime number generated in the given range are: ")
    for i in range(start,end+1):
        for j in range(2,(i//2)+1):
            if(i%j==0):
                break
        else:
            if(i!=1):
              print(i,end=" ")
            
start=int(input("Enter start range:"))
end=int(input("Enter end range:"))
prime(start,end)

