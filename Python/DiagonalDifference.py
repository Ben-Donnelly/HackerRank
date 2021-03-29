class Solution:
	def __init__(self, arr):
		self.a = arr
		self.len = len(arr)

	def comp_diag(self):
		# rtl = []
		# ltr = []


		# for k, v in enumerate(self.a):
		# 	rtl.append(v[k])
		# 	ltr.append(v[-k - 1])

		# return abs(sum(rtl) - sum(ltr))

		return abs(sum(v[k] - v[-k - 1] for k, v in enumerate(self.a)))



test = Solution([[11, 2, 4], [4, 5, 6], [10, 8, -12]])
run = test.comp_diag()

print(run)