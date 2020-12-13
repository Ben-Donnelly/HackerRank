class Solution:
	def __init__(self, c):
		self.clouds = c

	def joc(self):

		i = 0
		count = 0
		length = len(self.clouds)

		while i < length-1:
			if i < length-2 and self.clouds[i+2] == 0:
				i += 2
			else:
				i += 1
			count += 1

		return count


test = Solution([0, 0, 0, 1, 0, 0])
run = test.joc()

print(run)
