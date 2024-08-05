class Solution:
	def myPow(self, x, n) -> bool:
		# if n == 1:
		# 	return True
		# if n % 2 != 0 or n == 0:
		# 	return False
		# return self.isPowerOfTwo(n/2)
		a = 0
		if n == 0:
			return 1
		if n == 1:
			return x
		if n > 0:

			a = self.myPow(x, n // 2)
			if n % 2 == 0:
				return a * a
			elif n % 2 == 1:
				return x * a * a
		if n < 0:
			n = abs(n)
			a = self.myPow(1 / x, n // 2)
			if n % 2 == 0:
				return a * a
			elif n % 2 == 1:
				return 1 / x * a * a