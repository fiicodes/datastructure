class Solution:
    def maxLen(self, n, arr):
        prefix_sum = {}  # Dictionary to store prefix sums and their indices
        max_length = 0
        current_sum = 0

        for i in range(n):
            current_sum += arr[i]

            # If the current sum is zero, then the subarray from the beginning to the current index has a sum of zero
            if current_sum == 0:
                max_length = i + 1

            # If the current sum is already present in the prefix_sum dictionary,
            # it means there exists a subarray with a sum of zero between the stored index and the current index.
            # Update the max_length if the current subarray is longer.
            if current_sum in prefix_sum:
                max_length = max(max_length, i - prefix_sum[current_sum])
            else:
                # If the current sum is not present in the dictionary, store it with its index.
                prefix_sum[current_sum] = i

        return max_length
