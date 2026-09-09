import numpy as np
# array1=np.arange(1,10)
# array2=np.arange(1,10).reshape(3,3)
# print(array1.shape)
# print(array2.shape)
# print(array1.type)
# print(array2.type)

# a=np.array([10,20,30,40])
# b=np.array([1,2,3,4])
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)



# data=np.array([[10,20,30],[40,50,60],[70,80,90]])
# print(np.sum(data,axis=1))
# print(np.sum(data,axis=0))
# print(np.max(data))
# print(np.min(data))
# print(np.mean(data))



marks=np.array([78,85,90,66,72,88,95,60])
print(np.mean(marks))
print(np.median(marks))
print(np.var(marks))
print(np.std(marks))
print(np.min(marks))
print(np.max(marks))

print(np.sort(marks))

print(np.percentile(marks,25))
print(np.percentile(marks,50))
average_marks=np.average(marks)
print(np.sum(marks>average_marks))



