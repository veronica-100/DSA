import ast
#class Solution(object):
    #def addToArrayForm(self, num, k):
        #a = reduce(lambda x, y: k + )
        #a = int(''.join(map(str, num)))  # convert array into int string
        #a = a + k
        #b = str(a)
        #c = ast.literal_eval(b)
        #return c
class Solution:
  def addToArrayForm(self, num, k):
    for i in reversed(range(len(num))):
      k, num[i] = divmod(num[i] + k, 10) # 'divmod(n, d)' = 'n // d, n % d')

    while k > 0:
      num = [k % 10] + num
      k //= 10
    
    return num

aa = Solution()
print(aa.addToArrayForm([1, 2, 0, 0], 34))
