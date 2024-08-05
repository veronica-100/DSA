from collections import Counter
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count = Counter(arr)
        for a in arr:
            if count[a] == 1:
                k -= 1
                if k == 0:
                    return a

        return ''

aa = Solution()
print(aa.kthDistinct(["d","b","c","b","c","a"], 2))