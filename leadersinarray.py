class Solution:
    # Function to find the leaders in the array.
    def leaders(self, n, arr):
        leaders = []
        max_from_right = arr[-1]  # Start with the rightmost element
        leaders.append(max_from_right)

        # Traverse the array from right to left
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                max_from_right = arr[i]
                leaders.append(max_from_right)

        # Reverse the list as we added leaders from right to left
        leaders.reverse()
        return leaders