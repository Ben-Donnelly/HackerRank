class Solution:
	def __init__(self, s, d, m):
		self.l = s
		self.day = d
		self.month = m

	def birthday(self):
		# Below to one line because Python
		return sum([1 for i in range(len(self.l)-self.month+1) if sum(self.l[i:i+self.month]) == self.day])
		# c = 0

		# we have a sliding window of size n
		# therefore if whats left to check is < n dont bother checking it
	    # Pretty negligable but for massive numbers it would save time


		# for i in range(len(self.l)-self.month+1):
		# 	if sum(self.l[i:i+self.month]) == self.day:
		# 		c += 1
		# print(c)


test = Solution([1, 2, 1, 3, 2], 3, 2)
run = test.birthday()

print(run)