class Solution:
	def __init__(self, a, k, queries):
		self.list = a
		self.num_rotations = k
		self.queries = queries

	def circular_array_rotation(self):
		# % len(list) incase k > len(list)
		rot_by = -self.num_rotations % len(self.list)
		# Rotating the list
		self.list = self.list[rot_by:] + self.list[:rot_by]

		return [self.list[i] for i in self.queries]


test = Solution([1, 2, 3], 2, [0, 1])
run = test.circular_array_rotation()

print(run)