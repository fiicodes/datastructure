class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        max_elem=max(arr)

        curr_winner=arr[0]
        curr_streak=0
        if k>=len(arr):
            return max_elem

        for i in range(1,len(arr)):
            if curr_winner>arr[i]:
                curr_streak+=1

            else:
                curr_streak=1
                curr_winner=arr[i]
            if curr_streak==k or curr_winner==max_elem:
                return curr_winner
        return curr_winner
















