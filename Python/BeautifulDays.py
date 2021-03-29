class Solution:
	def __init__(self, i, j, k):
		self.start = i
		# +1 here so we dont have to do it in the loop below
		self.end = j + 1
		self.div = k

	def b_d_conversion(self):
		c = 0
		for i in range(self.start, self.end):
			rev_num = int(str(i)[::-1])

			if abs(i - rev_num) % self.div == 0:
				c += 1
		return c

	def b_d_no_conversion(self):
		c = 0

		for i in range(self.start, self.end):
			rev_num = 0
			temp = i
			while temp > 0:
				rev_num = rev_num*10 + temp % 10
				temp //= 10

			if abs(i - rev_num) % self.div == 0:
				c += 1
		return c


test = Solution(20, 23, 6)
run = test.b_d_conversion()

print(run)