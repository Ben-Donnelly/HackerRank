class Solution:
	def __init__(self, x1, v1, x2, v2):
		self.x1 = x1
		self.x2 = x2
		self.v1 = v1
		self.v2 = v2

	def kangaroo(self):
		# If the velocity of k1 < velocity of k2, they can never meet
		if self.v1 < self.v2:
			return "NO"

		for i in range(10000):
			if self.v1 * i + self.x1 == self.v2 * i + self.x2:
				return "YES"

		return "NO"


test = Solution(0, 3, 4, 2)
run = test.kangaroo()

print(run)

