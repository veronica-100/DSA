class Solution(object):
     def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
         """
         d = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
         num = 0
         for i in n:
             num = num * 10 + d[i]
        return num
         num3 = func2(num1) + func2(num2)
         print(str(num3))

aa = Solution()
aa.addStrings("1200","123")