class Solution:
	def __init__(self, x, y, z):
		self.c1 = x
		self.c2 = y
		self.m = z

	def distance(self, cat):
		return abs(self.m - cat)

	def cat_and_mouse(self):
		a = self.distance(self.c1)
		b = self.distance(self.c2)

		if a > b:
			return "Cat A"
		
		if a < b:
			return "Cat B"

		return "Mouse C"


test = Solution(1, 4, 3)
run = test.cat_and_mouse()

print(run)
