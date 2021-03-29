class Solution:
	def __init__(self, scores):
		self.scores = scores

	def breakingRecords(self):
		lovest = highest = self.scores[0]

		h_c = 0
		l_c = 0

		for i in self.scores:
			if i > highest:
				h_c += 1
				highest = i
			if i < lovest:
				l_c += 1
				lovest = i
		return h_c, l_c


test = Solution([10, 5, 20, 20, 4, 5, 2, 25, 1])
run = test.breakingRecords()

print(*run)

