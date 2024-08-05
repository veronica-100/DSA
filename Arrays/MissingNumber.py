class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = Counter(s)
        print(d.most_common())
        t = ""
        sorted_d = sorted(d.items(), key=lambda x :x[1], reverse = True)
        for i, j in sorted_d.items():
            t += i*j
        return t