class Solution:
	def __init__(self, arr):
		self.a = arr

	def simpleArraySum(self):
		return sum(self.a)

		# sum_l = 0
		# for i in self.a:
		# 	sum_l += i
		# print(sum_l)

test = Solution([1, 2, 3, 4, 5])
run = test.simpleArraySum()

print(run)