employee=["Ram","Shyam","Harish","Ramesh"]
employee_id=[1,4,23,21]
salary=[40000,50000,60000,70000]

#zip() to create zip object
zipobj=zip(employee,employee_id,salary)
#convert zip object as set
zipobj=set(zipobj)
print("The zipped object:",zipobj)
'''The zipped object: {('Ram', 1, 40000), ('Harish', 23, 60000)
                    , ('Shyam', 4, 50000), ('Ramesh', 21, 70000)}
'''

#unzipped the values in different list
ename,eid,esal=zip(*zipobj)
#print lists
print("Employee name:",ename)
print("Employee ID:",eid)#Employee ID: (4, 23, 21, 1)
print("Employee Salary:",esal)
