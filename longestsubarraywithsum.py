def longestSubarrayWithSumK(a: [int], k: int) -> int:

    subarrays = []
    current_sum = 0
    start = 0
    for i in range(len(a)):
        current_sum+=a[i]
        while current_sum>k:
            current_sum-=a[start]
            start+=1
        if current_sum==k:
            subarrays.append(a[start:i+1])
    maxList = max(subarrays, key=len)
    maxLength = len(maxList)

    return  maxLength



