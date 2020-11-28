class Solution:
	def __init__(self, s, t, a, b, apples, oranges):
		self.house_start = s
		self.house_end = t
		self.a_loc = a
		self.o_loc = b
		self.a_lis = apples
		self.o_lis = oranges

	def count(self, loc, lis):
		return sum(i + loc in range(self.house_start, self.house_end + 1) for i in lis)

	# Complete the countApplesAndOranges function below.
	def countApplesAndOranges(self):
		a_c = self.count(self.a_loc, self.a_lis)
		b_c = self.count(self.o_loc, self.o_lis)

		return [a_c, b_c]


test = Solution(7, 11, 5, 15, [-2, 2, 1], [5, -6])
run = test.countApplesAndOranges()

print(*run, sep="\n")


