ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#Sorting the given list
ages.sort()
print("1. The sorted list of the given ages:", ages,"\n")
print("\tThe min age is:", min(ages),"\n")
print("\tThe max age is:", max(ages),"\n")

#Adding the min age and the max age again to the list
ages.append(19)
ages.append(26)
print("2. The list is:", ages,"\n")

#The median age

import statistics as st

list_median_age = st.median(ages)
print("3. The median age of the list given is:", list_median_age,"\n")

#Find the average age

from statistics import mean


list_mean = mean(ages)
print("4. The average age of the list is:", list_mean,"\n")

#The range of the ages (max minus min)



maximum_age = max(ages)
minimum_age = min(ages)
range_of_ages = maximum_age - minimum_age
print("5. The range of the ages is:", range_of_ages,"\n")
