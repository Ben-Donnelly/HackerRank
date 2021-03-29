class LeftRot:
	def __init__(self, len):
		self.a = [i+1 for i in range(len)]
		self.len = len

	def rot_left(self, num):
		print(self.a[-(self.len - num):]+ self.a[:num])

test = LeftRot(5)

test.rot_left()