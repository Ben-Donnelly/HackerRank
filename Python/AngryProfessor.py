class Solution:
	def __init__(self, k, a):
		self.threshold = k
		self.times = a

	def angry_prof(self):
		print(sum(1 for arrival in self.times if arrival <= 0))
		return "NO" if sum(1 for arrival in self.times if arrival <= 0) >= self.threshold else "YES"


test = Solution(2, [0, -1, 2, 1])
run = test.angry_prof()

print(run)

