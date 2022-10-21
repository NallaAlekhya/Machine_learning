import numpy as np
 
x=np.random.randint(1,20,15)

print("Original array")
print(x)

a=x.reshape(3,5)
print("Array reshaped")
print(a)


print("Setting max value to 0")
a = np.where(a==[[i] for i in np.amax(a,axis=1)],0,a)
print(a)
