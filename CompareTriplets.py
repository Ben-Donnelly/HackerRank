class Solution:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def comp(self):
		# x = sum([i > j for i, j in zip(self.a, self.b)])
		# y = sum([i < j for i, j in zip(self.a, self.b)])
		#
		# return [x, y]
		
		scores = [0, 0]
		# We know the length is always 3
		for i in range(3):
			if self.a[i] > self.b[i]:
				scores[0] += 1
			else:
				scores[1] += 1

		return scores
test = Solution([1, 2, 3], [3, 2, 1])
run = test.comp()

print(run)