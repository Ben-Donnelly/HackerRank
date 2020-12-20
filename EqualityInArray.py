from collections import Counter
class Solution:
	def __init__(self, arr):
		self.list = arr

	def eia_1(self):
		x = set(self.list)
		ret = []
		for i in x:
			ret.append(self.list.count(i))

		ret.remove(max(ret))
		return sum(ret)

	def eia_2(self):
		temp = Counter(self.list)
		return len(self.list) - max(temp.values())

test = Solution([3, 3, 2, 1, 3])
run = test.eia_1()

print(run)