class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t = list(t)
        for i in s:
            if i in t:
                t.remove(i)
        return "".join(t)

aa = Solution()
aa.findTheDifference("", "y")