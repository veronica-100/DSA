class Solution(object):
    def numTeams(self, values):
        """
        :type rating: List[int]
        :rtype: int
        """
        a = 0
        b = 0
        for i in range(len(values)):
            for j in range(i, len(values)):
                a = values[i] + values[j] + i - j
                b = max(a, b)
                a = 0
        return b