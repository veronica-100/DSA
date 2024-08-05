class Solution(object):
    def nextGreaterElements(self, nums):
        # run Next Greater Element I two times
        n = len(nums)
        s = nums[::-1]
        res = []
        for i in range(n - 1, -1, -1):
            if not s:
                res.append(-1)
            elif s and s[-1] > nums[i]:
                res.append(s[-1])
            elif s and s[-1] <= nums[i]:
                while s and s[-1] <= nums[i]:
                    s.pop()
                if not s:
                    res.append(-1)
                else:
                    res.append(s[-1])
            s.append(nums[i])
        print(res[::-1])