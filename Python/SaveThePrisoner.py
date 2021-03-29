class Solution:
	def __init__(self, n, m, s):
		self.num_pris = n
		self.num_sweets = m
		self.start_pos = s

	def save_p(self):
		warn = (self.num_sweets + self.start_pos - 1) % self.num_sweets
		# "Indexed" at 1 so if 0 were at the last prisoner
		return warn if warn else self.num_pris


test = Solution(3, 7, 3)
run = test.save_p()

print(run)
