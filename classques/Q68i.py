#By list commprehension
def cubelc():
    l=[x**3 for x in range(1,31)]
    return(l)
print("List Comprehension generated result:",cubelc())
