def insertionsort(arr):
    for i in range(1,len(arr)):
        anchor=arr[i]
        j=i-1
        while j>=0 and anchor<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=anchor

if __name__=='__main__':

    arr=[3,56,89,9,77,12]
    insertionsort(arr)
    print(arr)
