
def find_all_subarrays_with_sum(nums, target_sum):
    subarrays = []
    current_sum = 0
    start = 0
    for i in range(len(nums)):
        current_sum+=nums[i]
        while current_sum>target_sum:
            current_sum-=nums[start]
            start+=1
        if current_sum==target_sum:
            subarrays.append(nums[start:i+1])
    return subarrays


