from time import time
from operator import itemgetter
class Solution:
	def __init__(self, n, p):
		self.num_pages = n
		self.target = p

	def page_count1(self):
		t1 = t2 = 0
		x = [(i, i+1) for i in range(0, self.num_pages+1, 2)]
		for i in x:
			if self.target in i:
				t1 = x.index(i)

		x.reverse()
		for i in x:
			if self.target in i:
				t2 = x.index(i)

		# print(t1, t2)
		print(min(t1, t2))

	def page_count2(self):
		x = [(i, i+1) for i in range(0, self.num_pages+1, 2)]
		# If the length of the list is 1, we know the page is the first one
		if len(x) == 1:
			return 0

		# Largest value of smallest half
		# Could use lambda functions, assume libraries allowed (allowed on HR)
		max_o_min = max(x[:len(x) // 2], key=itemgetter(1))[1]

		# If our target is <= the largest value of the smallest half
		# We know left -> right traversal will be the smallest
		if self.target <= max_o_min:
			for item in x[:len(x) // 2]:
				if self.target in item:
					return x.index(item)
				
		# Otherwise its the larger side
		for item in x[len(x) // 2:]:
			if self.target in item:
				return len(x) - 1 - x.index(item)

	def page_count_maths(self):
		return min(self.target // 2, self.num_pages // 2 - self.target // 2)


test = Solution(6, 2)
run = test.page_count_maths()

print(run)
