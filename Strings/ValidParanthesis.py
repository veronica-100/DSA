class Solution(object):
     def isValid(self, s: str) -> bool:
         dt = {'(': ')', '[': ']', '{': '}'}
         stack = []
         for i in s:
             if i == '(' or i == '[' or i == '{':
                 stack.append(i)
             else:
                print(dt[stack[-1]])
                 if not stack or i != dt[stack[-1]]:
                     return False
                 else:
                    stack.pop()
        if stack:
             return False
        else:
             return True

 aa = Solution()
 aa.isValid("([]{}")