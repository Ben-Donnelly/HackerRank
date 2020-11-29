class Solution:
	def __init__(self, bill, k, b):
		self.bill = bill
		self.ne = k
		self.a_contrib = b

	def bon_appetit(self):
		self.bill.pop(self.ne)

		x = self.a_contrib - sum(self.bill) // 2
		return x if x else "Bon Appetit"


test = Solution([3, 10, 2, 9], 1, 12)
run = test.bon_appetit()

print(run)
