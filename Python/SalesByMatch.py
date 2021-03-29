class Solution:
	def __init__(self, n, ar):
		self.number = n
		self.l = ar

	def sock_merchant(self):
		# if even num e.g. 4 , 4//2 == 2, 0 socks left over
		# if odd, 7//2 == 3, 1 sock left over
		# Therefore we will have the correct number of pairs
		return sum([self.l.count(i)//2 for i in set(self.l)])


test = Solution(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
run = test.sock_merchant()

print(run)