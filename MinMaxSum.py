class Solution:
	def __init__(self, arr):
		self.l = arr

	def miniMaxSum(self):
		x = sum(self.l)
		print(x-max(self.l), x-(min(self.l)))
		# min = 100000000
		# max = -1
		# for i in range(len(self.l)):
		# 	t = self.l[i]
		# 	self.l[i] = 0
		#
		# 	if sum(self.l) > max:
		# 		max = sum(self.l)
		# 	if sum(self.l) < min:
		# 		min  = sum(self.l)
		# 	self.l[i] = t

		# print(min, max)







test = Solution([1, 2, 3, 4, 5])
run = test.miniMaxSum()

print(run)