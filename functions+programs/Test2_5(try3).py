'''file_path="non_writeable_file.txt"
try:
    with open(file_path,"w") as file:
         file.write("Hello, World!")
except IOError as e:
    print(f"Error: {e}")
finally:
    print("Always executed.")
'''

#file_path="non_writeable2_file.txt"
file_path=input("Enter the file path without .txt extension :")+".txt"
print(file_path)
try:
    file=open(file_path,'w')
except IOError:#result of incorrect file name or location
    print("Unable to create file on disk")
    file.close()
finally:
    file.write("Hello, World!")
    file.close()
