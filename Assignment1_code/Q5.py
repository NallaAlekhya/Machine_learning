PI_value = 3.14
given_radius=30

#When radius is 30

of_circum_of_circle_ = 2 * PI_value * given_radius
of_area_of_circle =PI_value * given_radius * given_radius

print("The circumference of the circle with radius 30 meters is" ,of_circum_of_circle_,"\n")
print("The area of the circle with radius 30 meters is" ,of_area_of_circle,"\n")
print("**************************\n")



#taking user's input

radius = float(input(' Please Enter the radius of a circle: '))
user_circumference = 2 * PI_value * radius
user_area = PI_value * radius * radius

print(" Circumference Of a Circle = %.2f" %user_circumference)
print(" Area Of a Circle = %.2f" %user_area)
