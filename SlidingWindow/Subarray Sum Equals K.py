class Solution(object):
    def maxSum(self, arr, k):
        n = len(arr)
        totalSum = sum(arr)

        # k must be smaller than n
        if (n < k):
            print("Invalid")
            return -1

        # Compute sum of first
        # window of size k
        res = 0
        for i in range(k):
            res += arr[i]

        # Compute sums of remaining windows by
        # removing first element of previous
        # window and adding last element of
        # current window.
        curr_sum = res
        for i in range(k, n):
            curr_sum += arr[i] - arr[i - k]
            res = max(res, curr_sum)

        print(totalSum - res)