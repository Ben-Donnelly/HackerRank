from string import ascii_lowercase
class Solution:
	def __init__(self, heights):
		self.heights = dict(zip(ascii_lowercase, heights))

	def designer_pdf_viewer(self, word):

		m = max([self.heights[i]  for i in set(word)])
		return m * len(word)


test = Solution([1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7])
run = test.designer_pdf_viewer('zaba')

print(run)