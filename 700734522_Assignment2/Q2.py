import pandas as Pandas
import re
import matplotlib.pyplot as plt

file=Pandas.read_csv("data.csv")
print("question 1\n")
print(file)

print("\n")

#2
print("\n question 2 \n")
print("Basic statistical description about the data.\n")
print(file.describe())

print("\n*******************************\n")

#3
print("\n question 3 \n")
print(file['Calories'].isna().sum())
print(file['Calories'].mean())
print(file)
file=file.fillna(file.mean())
print(file)
print("\n*******************************\n")
#4
print("\n question 4 \n")
print(file.groupby('Duration').agg({'Maxpulse': ['mean', 'min', 'count', 'max']}))
print("\n*******************************\n")

#5
print("\n question 5 \n")
print(file[(file['Calories']>500) & (file['Calories']<1000)])
print("\n*******************************\n")

#6
print("\n question 6 \n")
print(file[(file['Calories']>500) & (file['Pulse']<100)])
print("\n*******************************\n")


#7
print("\n question 7 \n")
file_modified=file.drop("Maxpulse",axis=1)
print(file_modified)
print("\n*******************************\n")

#8
print("\n question 8 \n")
print(file.drop("Maxpulse",axis=1))
print("\n*******************************\n")

#9
print("\n question 9 \n")
file["Calories"] = file["Calories"].astype(float).astype(int)
print(file)
print("\n*******************************\n")

#10
print("\n question 10 \n")
file.plot.scatter(x='Duration',y='Calories')
plt.show()
print("\n*******************************\n")
