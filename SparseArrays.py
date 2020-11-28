class Solution:
	def __init__(self, strings, queries):
		self.strings = strings
		self.queries = queries

	def matching_strings_naive(self):
		ret = []
		for i in self.queries:
			count = 0
			for j in self.strings:
				if i == j:
					count += 1

			ret.append(count)
		return ret

	def matching_strings_better(self):
		return [self.strings.count(i) for i in self.queries]

test = Solution(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc'])

print(test.matching_strings_naive())
print(test.matching_strings_better())