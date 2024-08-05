# class Solution(object):
#     def addToArrayForm(self, num, k):
#         """
#         :type num: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         a = ''.join(map(str, num)) # convert array into string
#         a = int(a)
#         a = a + k
#         b = str(a)
#         l = [i for i in b]
#         return l
#
# aa = Solution()
# aa.addToArrayForm([1,2,0,0],34)