pounds_list = []

kilo_list = []
  
#Taking user input for the number of students
n = int(input("Enter number of students : "))

  

print("Enter pounds weights of the students")
for i in range(0, n):
    ele = int(input())

    pounds_list.append(ele)
    
print("The weights in kilograms entered are:" ,pounds_list)

kilogram=[i*0.453592 for i in pounds_list]

#appending the calculated kilo gram to the list
kilo_list.append(kilogram) 
      
print((kilo_list))
