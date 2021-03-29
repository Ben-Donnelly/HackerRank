class Solution:
	def __init__(self, c, k):
		self.list = c
		self.jump = k
		self.l_len = len(c)

	def j_o_c(self):
		i = 0
		energy = 100
		while True:
			energy -= 3 if self.list[i] == 1 else 1
			i += self.jump
			i %= self.l_len

			if not i:
				break

		return energy


test = Solution([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3)
run = test.j_o_c()

print(run)
