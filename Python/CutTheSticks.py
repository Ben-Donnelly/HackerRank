class Solution:
	def __init__(self, arr):
		self.list = sorted(arr, reverse=True)

	def cts(self):
		ret = []
		while self.list:
			ret.append(len(self.list))
			take_away = self.list.pop()
			while self.list and self.list[-1] <= take_away:
				self.list.pop()
		return ret


test = Solution([1, 2, 3, 4, 3, 3, 2, 1])
run = test.cts()

print(*run, sep="\n")