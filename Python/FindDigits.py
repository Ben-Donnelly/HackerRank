class Solution:
	def __init__(self, n):
		self.number = n

	def find_digits(self):
		orig_num = self.number
		num_digs = 0

		while self.number:
			temp = self.number % 10
			self.number //= 10

			if temp and not orig_num % temp:
				num_digs += 1
		return num_digs


test = Solution(1012)
run = test.find_digits()

print(run)
