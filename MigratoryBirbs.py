# Yes 'Birbs'
from collections import Counter
class Solution:
	def __init__(self, l):
		self.l = l

	def mb(self):
		# # 5 bird types
		# x = [0] * 5
		#
		# # 0 wont be used so -1 for index
		# for t in self.l:
		# 	x[t-1] += 1
		#
		# # compensate for -1 index
		# return x.index(max(x))+1

		# With library
		self.l.sort()
		res = Counter(self.l)
		return max(Counter(self.l), key=res.get)


test = Solution([1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4])
run = test.mb()

print(run)