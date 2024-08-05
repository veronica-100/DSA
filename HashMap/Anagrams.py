class Solution2(object):
    def findAnagrams(self, s, p):

        count1 = Counter(p)
        count2 = Counter(s[:len(p)])
        i, j = 0, len(p)
        size = len(s)
        ans = []
        while j <= size:
            if count2 == count1:
                ans += i,
            if j < size:
                count2[s[j]] += 1
            count2[s[i]] -= 1
            if count2[s[i]] == 0:
                del count2[s[i]]
            i += 1
            j += 1
        return ans