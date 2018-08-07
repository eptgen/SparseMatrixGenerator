
class SparseMatrix(object):
	def __init__(self):
		self.vals = {}
	def __repr__(self):
		return self.vals.__repr__()
	def get(self, i, j):
		if (i, j) in self.vals.keys():
			return self.vals[(i, j)]
		else:
			return 0
	def set(self, i, j, val):
		if val == 0:
			if (i, j) in self.vals.keys():
				del self.vals[(i, j)]
		else:
			self.vals[(i, j)] = val
	def to_dense(self, n):
		result = []
		for i in range(n):
			result.append([])
			for j in range(n):
				result[i].append(round(self.get(i, j)))
		return result
		