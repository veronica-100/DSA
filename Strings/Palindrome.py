class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = ''.join(ch for ch in s if ch.isalnum())
        print(s)
        return s == s[::-1]

aa = Solution()
aa.isPalindrome("A man, a plan, a canal: Panama")
