user_radius=int(input ("Input the radius of the circle : "))#taking the input from user
result_area=int(3.14 * user_radius ** 2)#calculating the area with the given formula
print_result="The area of a circle with radius {radius} is {result:.2f} meters square".format(radius=user_radius,result=result_area)#string formatting method
print(print_result)
