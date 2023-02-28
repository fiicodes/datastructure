A=[22,76,4,45,36]
for i in range(len(A)):
    min=i
    for j in range(i+1,len(A)):
        if A[min]>A[j]:
            min=j
    A[min],A[i]=A[i],A[min]
print("The sorted array is ")
for i in range(len(A)-1):
    print(A[i])

