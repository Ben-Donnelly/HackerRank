class Solution:
	def __init__(self, n):
		# We know the value on the first day so we can get rif of it
		self.num = n - 1

	def viral_advertising(self):
		cumulative = liked = 2

		for _ in range(self.num):
			liked += liked // 2
			cumulative += liked

		return cumulative


test = Solution(5)
run = test.viral_advertising()

print(run)
