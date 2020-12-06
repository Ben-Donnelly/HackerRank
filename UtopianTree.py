class Solution:
	def __init__(self, n):
		self.cycles = n

	def xxxxxxxx(self):
		height = 1
		for i in range(self.cycles):
			if i % 2 == 0:
				height *= 2
			else:
				height += 1
		return height



test = Solution(5)
run = test.xxxxxxxx()

print(run)