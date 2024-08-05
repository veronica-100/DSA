class Solution:
    def nextPermutation(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[i - 1]:  # here must be <= to take care of the duplicates!
            i -= 1

        if i == 0:
            self.swap(nums, 0, len(nums) - 1)
            return
        left_index = i - 1

        i = len(nums) - 1
        while nums[i] <= nums[left_index]:
            i -= 1
        nums[i], nums[left_index] = nums[left_index], nums[i]
        self.swap(nums, left_index + 1, len(nums) - 1)

    def swap(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1