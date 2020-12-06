class Solution:
	def __init__(self, height, k):
		self.height_l = height
		self.jump = k

	def hurdle_race(self):
		m = max(self.height_l)

		return max(0, m - self.jump)


test = Solution([1, 2, 3, 3, 2], 3)
run = test.hurdle_race()

print(run)
