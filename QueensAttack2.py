class Solution:
	def __init__(self, n, k, r_q, c_q, obstacles):
		self.r_a_c = n
		self.num_obs = k
		self.row = r_q
		self.col = c_q
		self.obs = obstacles

	# def queens_attack(self):
	# 	# Deal with duplicate obs
	# 	# Note: Lists are mutable (can change), use tuples (immutable)
	# 	obs_set = set([tuple(item) for item in self.obs])
	#
	# 	count = 0
	# 	directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
	#
	# 	# get each value, in each tuple, e.g. r = 1, c = 0 -> r = 1, c = 1 -> r = 0, c = 1 ...
	# 	for r, c in directions:
	# 		# add our 'move' (r and c) to our queens position
	# 		temp_row = self.row + r
	# 		temp_col = self.col + c
	#
	# 		while True:
	# 			# check for obstacle
	# 			if (temp_row, temp_col) in obs_set:
	# 				break
	# 			# check if we have gone off the edge for rows and cols
	# 			if temp_row <= 0:
	# 				break
	# 			if temp_col <= 0:
	# 				break
	# 			if temp_row > self.r_a_c:
	# 				break
	# 			if temp_col > self.r_a_c:
	# 				break
	#
	# 			# if we haven't gone off the edge, and we haven't hit and obstacle
	# 			count += 1
	#
	# 			# follow the same path
	# 			temp_row += r
	# 			temp_col += c
	#
	# 	return count

	def queens_attack(self):
		# Deal with duplicate obs
		# Note: Lists are mutable (can change), use tuples (immutable)
		obs_set = set([tuple(item) for item in self.obs])

		count = 0
		directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

		# get each value, in each tuple, e.g. r = 1, c = 0 -> r = 1, c = 1 -> r = 0, c = 1 ...
		for r, c in directions:
			# add our 'move' (r and c) to our queens position
			temp_row = self.row + r
			temp_col = self.col + c

			# Check if we have gone off the edge or if were at an obstacle
			# This is done in if's above
			while 0 < temp_row <= self.r_a_c and 0 < temp_col <= self.r_a_c and (temp_row, temp_col) not in obs_set:

				# if we haven't gone off the edge, and we haven't hit and obstacle
				count += 1

				# follow the same path
				temp_row += r
				temp_col += c

		return count


# test = Solution(1000, 0, 4187, 5068, [])
# test = Solution(1000, 0, 4187, 5068, [[5, 5], [4, 2], [2, 3]])
test = Solution(5, 3, 4, 3, [[5, 5], [4, 2], [2, 3]])
run = test.queens_attack()

print(run)
