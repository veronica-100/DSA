class Solution2(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        j = len(s) - 1
        s = list(s)

        while i <= j:
            if not s[i].isalpha():
                i += 1
                continue
            if not s[j].isalpha():
                j -= 1
                continue
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        print(''.join(s))

aa = Solution2()
aa.reverseOnlyLetters("a-bC-dEf-ghIj")