class Solution:
	def __init__(self, n, k, ar):
		self.len = n
		self.div = k
		self.l = ar

	def dsp(self):
		# count = 0
		# for i in range(len(self.l)):
		# 	for j in range(i+1, len(self.l)):
		# 		x = self.l[i]
		# 		y = self.l[j]
		# 		if (x + y) % self.div == 0:
		# 			count += 1
		# return count
		return sum([1 for i in range(len(self.l)) for j in range(i+1, len(self.l)) if (self.l[i] + self.l[j]) % self.div == 0])



test = Solution(6, 3, [1, 3, 2, 6, 1, 2])
run = test.dsp()

print(run)