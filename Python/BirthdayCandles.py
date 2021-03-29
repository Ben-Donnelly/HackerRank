class Solution:
	def __init__(self, candles):
		self.l = candles

	def birthdayCakeCandles(self):
		return self.l.count(max(self.l))


test = Solution([3,2,1,3])
run = test.birthdayCakeCandles()

print(run)