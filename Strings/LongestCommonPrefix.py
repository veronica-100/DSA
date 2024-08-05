class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = sorted(strs)
        st = ""
        s = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(s)):
                if s[j] == strs[i][j]:
                    st += s[j]
                else:
                    s = st
                    break
            st = ""
        print(s)

    aa = Solution()
    aa.longestCommonPrefix(["flower", "flow", "flight"])