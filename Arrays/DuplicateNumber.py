class Solution(object):
    def merge(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        result = []
        for i in range(0, len(nums1)):
            for j in range(0, len(nums2)):
                if nums1[i] < nums2[j]:
                    result.append(nums1[i])
                else:
                    result.append(nums2[j])
        print(result)