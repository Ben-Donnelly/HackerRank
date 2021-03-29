class Solution:
	def __init__(self, a, b):
		self.list1 = a
		self.list2 = b

	def between_two_sets(self):
		maxOfMin = max(self.list1)
		minOfMax = min(self.list2)

		x = []
		for i in range(maxOfMin, minOfMax+1):
			if all(not i % y for y in self.list1):
				x.append(i)

		c = 0
		for i in x:
			if all(not y % i for y in self.list2):
				c += 1
		return c

test = Solution([2, 4], [16, 32, 96])
run = test.between_two_sets()

print(run)