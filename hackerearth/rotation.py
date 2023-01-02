t =int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(input().split())




    index=int(n)-(int(k)%int(n))
    l = a[index:]+a[:index]

    print(*l)



####other ans

testCase = int(input())



#code will run for that many testcase

i = 0

while i < testCase:

       #taking input for each testcase

       n, rotation = input().split()

       nums = list(map(int,input().split()))

      #actual logic

      #using mod operator to handle rotations greater that the length of input list

       rotation = int(rotation) % int(n)

      #splitting the list into two parts first part will be till the rotation point and second part will be from rotation point to the end, then prepend the second part to first one to simulate rotated array.

       print(" ".join(str(x) for x in nums[-int(rotation):] + nums[:-int(rotation)]))

       i+=1


