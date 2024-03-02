def longestSubarrayWithSumK(a: [int], k: int) -> int:
        cursum=0
        subarray=[]
        start=0
        for i in range(len(a)):
            cursum+=a[i]
            while cursum > k:
                cursum-=a[start]
                start+=1
            if cursum==k:
                subarray.append(a[start:i+1])
        maxarray=max(subarray,key=len)
        maxlen=len(maxarray)
        return  maxlen



