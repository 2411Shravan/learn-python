result={}
result['shravan']=30
result['shreyas']=35
result['praveen']=40
result['chandan']=45
result['ashik']=50
print(result)
#to print specific data-->
print(result['ashik'])
#to amend the data just-->
result['shravan']=45
print(result)
#fetch only keys from dictionaries-->
kys=result.keys()
print(kys)
#fetch only values from dictionaries-->
vals=result.values()
print(vals)
#to convert dictionaries into lists-->
data=list(result.keys())
print(data)
data_vals=list(result.values())
print(data_vals)
#make a list of tuples from dictionaries in python -->
extra_vals=result.items()
print(extra_vals)
#delete item from dictionaries in python -->
del result['shravan']
print(result)
print(result.keys())
#taking dict input from user
em=True
extra={}
while(em):
    name=input('Enter the name of student : ')
    marks=int(input('Enter the marks of student : '))
    extra[str(name)]=marks
    
    ch=int(input(print("Do you wish to continue ? 0/1")))
    if(ch==1):
        em=True
    else:
        em=False


print(extra)
