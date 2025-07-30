#Given a dictionary
# employee={
#     "id":101,
#     "name":"Anjali",
#     "department":"HR",
#     "salary":450000
# }

#Print the department of employee
#Updates the salary to 50000
#print the updated salary
#Add a new key -value pair location:Bangalore to employee

#Given a string
# msg="Hello, Python World!"

#print the first character
#print the last character
#print the first 5 characters
#print the reverse
#print the length



#Given a set
# s={'dog','cat','rabbit','cow'}
#add a new animal "lion" to set
#print the updated set


#Given a list
# l=['Riya',"Ankit","Sara"."Manu"]
#Print the first student
#Changes the second value to Amit

#Add a new student Amal
#Print the length
#print the updated list

#5 key features of Python

#What is the difference between mutable and immutable type?Give example

#What are the Major datatypes in Python?








#Given a dictionary
# employee={
#     "id":101,
#     "name":"Anjali",
#     "department":"HR",
#     "salary":450000
# }

#Print the department of employee
#Updates the salary to 50000
#print the updated salary
#Add a new key -value pair location:Bangalore to employee

employee = {
    "id": 101,
    "name": "Anjali",
    "department": "HR",
    "salary": 450000
}

print(employee['department'])  
employee['salary'] = 50000
print(employee['salary'])  
employee['location'] = 'Bangalore'
print(employee)



#Given a string
# msg="Hello, Python World!"

#print the first character
#print the last character
#print the first 5 characters
#print the reverse
#print the length
msg = "Hello, Python World!"
print(msg[0])

print(msg[-1])

print(msg[:5])  
print(msg[::-1])  

print(len(msg))  





#Given a set
# s={'dog','cat','rabbit','cow'}
#add a new animal "lion" to set
#print the updated set

s = {'dog', 'cat', 'rabbit', 'cow'}
s.add('lion')
print(s)




#Given a list
# l=['Riya',"Ankit","Sara"."Manu"]
#Print the first student
#Changes the second value to Amit

#Add a new student Amal
#Print the length
#print the updated list

l = ['Riya', 'Ankit', 'Sara', 'Manu'] 
print(l[0])  
l[1] = 'Amit'
l.append('Amal')
print(len(l))  
print(l)



#What is the difference between mutable and immutable type?Give example

Mutable types are data types whose values can be changed after creation. You can add, update, remove elements  them.
# l = [1, 2, 3]
# l[0] = 100 


Immutable types are data types whose values cannot be changed after creation. Any modification creates a new object.
s = "hello"
s[0] = 'H'  

#What are the Major datatypes in Python?

int,float ,str , bool,list