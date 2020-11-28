import temp
class Solution:
	def __init__(self, arr):
		self.a = arr

	def pm(self):
		# p = sum(i > 0 for i in self.a)
		# n = sum(i < 0 for i in self.a)
		# z = sum(i == 0 for i in self.a)

		# In testing this is ~3x quicker
		p, n, z = 0, 0, 0
		for i in self.a:
			if i > 0:
				p += 1
			elif i < 0:
				n += 1
			else:
				z += 1

		length = len(self.a)
		return f"{p/length:.6f}\n{n/length:.6f}\n{z/length:.6f}"

test = Solution(temp.x)
run = test.pm()

print(run)