class Solution:
	def __init__(self, a, b):
		self.lower = a
		self.higher = b
		self.max = int(self.higher ** 0.5)

	def sherlock_and_squares(self):
		# Square root of higher number
		# We know that the numbers have to be <= to this
		count = 0

		for i in range(1, self.max + 1):
			# We know that the number ** 2 is going
			# to be < the upper bound (thanks to above)
			# So only need to check if its >= the lower bound
			if i ** 2 >= self.lower:
				count += 1

		return count

	def sherlock_and_squares_1(self):
		# Because Python
		return sum([1 for i in range(1, self.max + 1) if i ** 2 >= self.lower])


test = Solution(100, 1000)
run = test.sherlock_and_squares()

print(run)