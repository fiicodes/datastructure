class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


    #    we need to rotate the input array and then rotate the k item and then from k to end of the array
        k=k%len(nums)
        l,r=0,len(nums)-1
       #to catch higher k value
        while(l<r):
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1

        l,r=0,k-1
        while(l<r):
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1
            
        l,r=k,len(nums)-1
        while(l<r):
            nums[l],nums[r]=nums[r],nums[l]
            l,r=l+1,r-1









