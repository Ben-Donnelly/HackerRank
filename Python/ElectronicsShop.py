# import timeit


class Solution:
	def __init__(self, keyboards, drives, b):
		self.kbp = keyboards
		self.dp = drives
		self.bud = b

	def get_money_spent(self):
		x = [i+j for i in self.kbp for j in self.dp if i+j <= self.bud]

		return max(x) if x else -1


test = Solution([3, 1], [5, 2, 8], 10)
run = test.get_money_spent()

# Tested with timeit
# print(timeit.timeit(stmt=test, number=100000))

# 100000 runs with:
# [-1], sorted = 0.8350169000000001
# max, sorted = 1.0512786
# max, unsorted = 0.7977044999999999
print(run)
