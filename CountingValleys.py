class Solution:
	def __init__(self, steps, path):
		self.path = [i for i in path]
		self.steps = steps

	def countingValleys(self):
		sea_level = 0
		val = 0
		for i in self.path:
			if i == 'U':
				sea_level += 1
				if not sea_level:
					val += 1
			else:
				sea_level -= 1

		return val

		# print(self.steps, self.path)


test = Solution(8, 'UDDDUDUU')
run = test.countingValleys()

print(run)