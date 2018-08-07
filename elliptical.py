from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve
from math import sin
import numpy as np
from matplotlib.pyplot import contour, show

def gen_elliptical_square(h):
	m = int((1 - h) / h)
	result = lil_matrix((m**2, m**2))
	def imap(i, j):
		return m * i + j
#	3for i in range(m + 1):
#	result.set(imap(0, i), imap(0, i), 1)
	for i in range(m):
		for j in range(m):
			if i==0 or i==m-1 or j==0 or j==m-1:
				result[imap(i, j), imap(i, j)] = 1
			else:
				result[imap(i, j), imap(i, j)] = -4 * h**-2
				result[imap(i, j), imap(i - 1, j)] = h**-2
				result[imap(i, j), imap(i + 1, j)] = h**-2
				result[imap(i, j), imap(i, j - 1)] = h**-2
				result[imap(i, j), imap(i, j + 1)] = h**-2
	#for i in range(m + 1):
	#	result.set(imap(m + 1, i), imap(m + 1, i), 1)
	return result

shapes = {
	"square": gen_elliptical_square
}

def gen_elliptical(shape, h):
	return shapes[shape](h)
	
m = 50
h = 1 / (m + 1)
A = gen_elliptical("square", h)
print(A)
print()
# lst = res.to_dense(m**2)
"""
for i in lst:
	for j in i:
		print("{:5}".format(j), end="")
	print()
"""
	
# A = np.matrix(lst)
	
f = lambda x, y: sin(x) * y ** 2 + x
f_lst = []

for i in range(m):
	for j in range(m):
		if (m / 8 < i and 7 * m / 8 > i and m / 8 < j and m / 4 > j) or (m / 8 < i and m / 4 > i and m / 8 < j and 7 * m / 8 > j):
			f_lst.append(1)
		else:
			f_lst.append(0)

"""
for i in f_lst:
	print(i)
"""
	
u = spsolve(A, f_lst)
# print(u)

pretty_u = []
for i in range(m):
	pretty_u.append([])
	for j in range(m):
		pretty_u[i].append(u[i * m + j])
		
contour(pretty_u)
show()

		












































