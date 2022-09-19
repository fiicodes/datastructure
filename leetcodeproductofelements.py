# class Solution:
  
#  def productExceptSelf(self,nums:list):
#     new_arr = []

  
#     for i in range(len(nums)):
#         product = 1
      
#         for j in range(len(nums)):
#             if nums[i] != nums[j]:
#                 product *= nums[j]
#             new_arr.append(product)

#     return new_arr
# ob=Solution()
# nums= [1,0]
# o=ob.productExceptSelf(nums)
# print(o)


# def productExceptSelf(a, n):
 
#     prod = 1
#     flag = 0
 
#     for i in range(n):
 
#         # Counting number of elements
#         # which have value
#         # 0
#         if (a[i] == 0):
#             flag += 1
#         else:
#             prod *= a[i]
 
#     # Creating a new array of size n
#     arr = [0 for i in range(n)]
 
#     for i in range(n):
 
#         # If number of elements in
#         # array with value 0
#         # is more than 1 than each
#         # value in new array
#         # will be equal to 0
#         if (flag > 1):
#             arr[i] = 0
 
#         # If no element having value
#         # 0 than we will
#         # insert product/a[i] in new array
#         elif (flag == 0):
#             arr[i] = (prod // a[i])
 
#         # If 1 element of array having
#         # value 0 than all
#         # the elements except that index
#         # value , will be
#         # equal to 0
#         elif (flag == 1 and a[i] != 0):
#             arr[i] = 0
 
#         # If(flag == 1 && a[i] == 0)
#         else:
#             arr[i] = prod
 
#     return arr
 
 
# # Driver Code
# n = 2
# array = [1,0]
# ans = productExceptSelf(array, n)
 
# print(*ans)

def product1(num,n):
        flag=0
        prod=1
        for i in range(n):
            if num[i]==0:
                flag+=1
            else:
                prod*=num[i]
        arr=[0 for i in range(n)]
        
        for j in range(n):
            if flag>1:
                arr[j]=0
            elif flag==0:
                print("hhj")
                arr[j]=(prod // num[j])
            elif flag==1 and num[i]!=0:
                arr[j]=0
            else:
                arr[j]=prod
        return arr

n = 4
array = [1,2,3,4]
ans = product1(array, n)
 
print(*ans)




   