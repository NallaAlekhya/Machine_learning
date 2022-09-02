

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Finding the length 

print("Length of IT Companies:", len(it_companies))#used len() method

#Adding 'Twitter' to it_companies

it_companies.add('Twitter')
print("Updated set of it companies:", it_companies)

#Inserting multiple IT companies 

mult_companies = ["Cognizant", "Accenture", "Netflix"]
it_companies.update(mult_companies)#using update method for adding multiple items
print("After inserting multiple companies:", it_companies)

#Removing  the companies 

it_companies.discard("Cognizant")
print("Deleting one company from set:", it_companies)

#What is the difference between remove and discard

#When discard() is used to eliminate some value, it produces the same result as remove() 
#There will be no error raised if the set exists. If it does not exist, it will be deleted. With the help of the remove() method, 
#It will delete the value if it exists, otherwise it will raise an error.

#Joining A and B sets

C = A.union(B)
print("After joining sets:", C)

#Finding the A intersection B

D = A.intersection(B)
print("After intersection the set is:", D)

#finding whether is A subset of B

E = A.issubset(B)
print("Is A subset of B:", E)

#Finding whether  A and B disjoint sets

F = A.isdisjoint(B)
print("Are A and B disjoint sets:", F)

#Joining A with B and B with A sets

X = A.union(B)
Y = B.union(A)
print(" Joining A with B:", X)
print("\tJoining B with A:", Y)

#What is the symmetric difference between A and B

Z = A.symmetric_difference(B)
print(" Symmetric difference between A and B:", Z)

#Delete the sets completely

del A
print(" set A deleted:")
del B
print("set B deleted")

#Convert the ages to a set and compare the length of the list and the set

K = set(age)
print(" Converting list:", K)
s = len(K)
print(s)
p = len(age)
print(p)
if p==s:
    print("Identical")
else:
    print("Different")
