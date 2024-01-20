id=int(input("Enter the student id:"))
name=input("Enter the student name:")
contact=int(input("Enter the contact no:"))
percent=int(input("Enter the percentage:"))

#to create a file
#(executed once only as it will create that file if we run again then error as file already exists)
#f=open('80_studentinfo.txt','x')

#writing the above record to the file
#f=open('80_studentinfo.txt','w')
#lines=[f'Student id={id}',f'Student name{name}',f'Student contact no={contact}',f'Student percentage={percent}']

f=open('80_studentinfo.txt','r')

print("MENU:","1.Add new record","2.Delete record","3.Update existing record","4.Display all records",
      "5,Display particular record","6.Display top 5 scorers",sep="\n")
ch=int(input("Enter your choice:"))
match ch:
    case 1:
       id=int(input("Enter the student id:"))
       name=input("Enter the student name:")
       contact=int(input("Enter the contact no:"))
       percent=int(input("Enter the percentage:"))
       
    case 2:
        pass
    case 3:
        pass
    case 4:
        pass
    case 5:
        pass
    case 6:
        pass
    case _:
        print("Invalid choice:")
