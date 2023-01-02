n=int(input())

a=[]


for i in range(n):

    a.append(input())
    count=0

    for j in range(i):

       if a[j]<a[i]:

            count+=1





    print(count)