class Solution:
	def __init__(self, n):
		self.n = n

	def staircase(self):
		# If you *Really* want a one liner
		print("\n".join([f"{' ' * (self.n-i)}{'#' * i}" for i in range(1, self.n+1)]))
		# for i in range(1, self.n+1):
		# 	print(f"{' ' * (self.n-i)}{'#' *i}")



test = Solution(6)
run = test.staircase()

# print(run)