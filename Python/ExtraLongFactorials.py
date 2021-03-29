from math import factorial
class Solution:
	def __init__(self, n):
		self.number = n

	def e_l_f(self):
		ret = 1
		# Python doesn't care how big your number gets 😎
		for i in range(2, self.number + 1):
			ret *= i

		return ret

	def e_l_f_speed(self):
		# Python doesn't care how big your number gets 😎
		# Much, much quicker
		return factorial(self.number)


test = Solution(20)
run = test.e_l_f()

print(run)