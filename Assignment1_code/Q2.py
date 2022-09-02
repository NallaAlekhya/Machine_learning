#an empty dictionary called dog

dog = {}
print("1.An empty dictionary called dog", dog,"\n")

#Adding name, color, breed, legs, age to the dog dictionary

dog = {"name": "Julie", "color" : "brown", "breed" : "german shepherd", "legs" : "4", "age" : "5"}
print("2. Adding the elements to the dog dictionary", dog,"\n")

#Creating a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary

student = {'first_name':'Priya','last_name':'signh','gender':'F','age':'29','martial status':'Unmarried','skills':['Python','Java'],
           'country':'USA','city':'Overland park','address':'123 W 908 ter'}
print("3. Created student dictionary:",student,"\n")

#Get the length of the student dictionary

print("4.length of the student dictionary is:",len(student),"\n")

#Get the value of skills and check the data type, it should be a list

print("5. The value is :", student.get('skills'))
print(" The data type of the skills:",type(student['skills']),"\n")

#Modifying  the skills values 

student['skills'].append('C#')#appending the list 
student['skills'].append('SAP')
print("6. The updated list is:", student,"\n")

#Get the dictionary keys as a list

print("7. The dictionary keys as list:", student.keys(),"\n")#.keys() used to get the key 

#Get the dictionary values as a list

print("8. The  dictionary values as a list:", student.values(),"\n")#.values() used to get the values 
