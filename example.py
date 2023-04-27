def twosum(arr,target):
   result=[]
   visited_number=dict()
   for i in range(len(arr)):
        no_to_searched=target-arr[i]


        if no_to_searched in visited_number:
            result.append((arr[i],visited_number[no_to_searched]))

        else:
            visited_number[arr[i]]=arr[i]
   return result




print(twosum([1,2,3,4,5,6],9))

