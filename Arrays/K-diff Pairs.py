class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                print(nums[i],nums[j])
                if abs(nums[i] - nums[j]) == k and i < j:
                    count += 1
        print(count)