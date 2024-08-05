class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # intervals.sort()
        # merged = []
        # for interval in intervals:
        #     # if the list of merged intervals is empty or if the current
        #     # interval does not overlap with the previous, simply append it.
        #     if not merged or merged[-1][1] < interval[0]:
        #         print(interval[0])
        #         merged.append(interval)
        #         print(merged[-1][1])
        #     else:
        #         # otherwise, there is overlap, so we merge the current and previous
        #         # intervals.
        #         print(interval[1])
        #         merged[-1][1] = max(merged[-1][1], interval[1])
        #         print(merged[-1][1])
        #
        # return merged