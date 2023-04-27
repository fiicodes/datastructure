class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap={}
        res=[]
        for i in nums:
            if  i not  in hashmap:
                hashmap[i]=1
            else:
                 hashmap[i]+=1
        sorted_dict = dict(sorted(hashmap.items(),reverse=True, key=lambda x: x[1])[0:k])
        for i in sorted_dict.keys():
            res.append(i)

        return (res)



ob=Solution()
print(ob.topKFrequent( [1,1,1,2,2,3],2))