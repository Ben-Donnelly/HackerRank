class ReverseArray:
	def __init__(self, a):
		self.a = a

	def reverse_1(self):
		return self.a[::-1]

	def reverse_2(self):
		temp = []
		for i in reversed(self.a):
			temp.append(i)
		return temp

	def reverse_3(self):
		return list(reversed(self.a))

	def reverse_4(self):
		self.a.reverse()
		return self.a



test = ReverseArray([1, 2, 3, 4])

run = test.reverse_4()

print(run)
