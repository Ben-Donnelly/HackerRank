class Solution:
	def __init__(self, l):
		self.l = l

		# init dict to <values_in_list> : 0
		self.freq = dict.fromkeys(set(l), 0)

	def picking_numbers(self):

		for i in self.l:
			self.freq[i] += 1

		dict_iterator = iter(self.freq)
		prev = next(dict_iterator)

		cur_max = 0
		for i in dict_iterator:

			if i - prev == 1:
				cur_max = max(cur_max, self.freq[prev] + self.freq[i])

			prev = i

		return max(max(self.freq.values()), cur_max)
		# Deals with cases such as:
		# list only having 1 value
		# 2 values being 1 difference apart but
		# another (single) value is higher e.g.:
		# {97: 50, 99: 1, 4: 24, 5: 25}
		# 4 and 5 are 1 away and summed = to 49
		# but 97 has 50 entries (sub array of say 25 and 25)
		# (or any combination equaling to 50)



x = [4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5, 97, 4, 5, 97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5, 97, 4, 97, 97, 5, 4, 97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97, 5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]

test = Solution(x)
run = test.picking_numbers()

print(run)
