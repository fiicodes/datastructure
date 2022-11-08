# def max_sum(a:list)->int:
#     # a=[-2,3,2,-1]
#     current_max=max_global=a[0]
#     for i in range(1,len(a)):
#         current_max=max(a[i],a[i]+current_max)
#         if current_max>max_global:
#             max_global=current_max
#     return max_global
# print(max_sum([-2,1,-3,4,-1,2,1,-5,4]))

# def my_fu(st):
#     l1=[ch for ch in st if ch.isalpha()]
#     return ''.join(l1.pop() if ch.isalpha() else ch for ch in st)


# st='ab-cd-ef'
# print(my_fu(st))

# def my_fun(num):
#     data=[0]
#     for i in range(1,num+1):
#         data.append(data[i>>1] + int(i & 1))
#     return data
# num=6
# print(my_fun(num))


# def my_fun(nums):
#     c=0
#     for i,j in enumerate(nums):
#         if i > c:
#             return False
#             c=max(c,i+j)
#         return True
# if __name__=="__main__":
#     print(my_fun([3,2,1,0,4]))

# x='abcdef'
# i='a'
# while i in x:
#     x=x[1:]
#     print(i,end=" ")

# def oddsum(n):
#     t=0
#     r=[]
#     for i in range(1,n+1):
#         odd=2*i -1
#         t=t+odd
#         r.append(t)
#     return r

 