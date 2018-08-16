from scipy.sparse import coo_matrix
from scipy.sparse.linalg import spsolve
from math import sin
import numpy as np
from matplotlib.pyplot import contour, show

def gen_elliptical_cube(h):
	pass

def gen_elliptical_square(h, order):
	m = (round((1 - h[0]) / h[0]), round((1 - h[1]) / h[1]))
	ai = []
	aj = []
	av = []
	def imap(i, j):
		return m[1] * i + j
#	for i in range(m + 1):
#	result.set(imap(0, i), imap(0, i), 1)
	for i in range(m[0]):
		for j in range(m[1]):
			inds = (i, j)
			if i == 0 or i == m[0] - 1 or j == 0 or j == m[1] - 1:
				ai.append(imap(i, j))
				aj.append(imap(i, j))
				av.append(1)
			else:
				ai.append(imap(i, j))
				aj.append(imap(i, j))
				av.append(-2 * h[0]**-2 - 2 * h[1]**-2)
				ai.append(imap(i, j))
				aj.append(imap(i - 1, j))
				av.append(h[0]**-2)
				ai.append(imap(i, j))
				aj.append(imap(i + 1, j))
				av.append(h[0]**-2)
				ai.append(imap(i, j))
				aj.append(imap(i, j - 1))
				av.append(h[1]**-2)
				ai.append(imap(i, j))
				aj.append(imap(i, j + 1))
				av.append(h[1]**-2)
				for k in range(2):
					offcenter = 0
					if inds[k] < order / 2 - 1:
						offcenter = inds[k] - order / 2
					elif (m[k] - 1) - inds[k] < order / 2 - 1:
						offcenter = order / 2 - ((m[k] - 1) - inds[k])
					weights = finite_diff(order, offcenter)
					for l in range(len(weights)):
						weight = weights[l]
						
				
	#for i in range(m + 1):
	#	result.set(imap(m + 1, i), imap(m + 1, i), 1)
	#print(ai)
	#print(aj)
	#print(av)
	return coo_matrix((av, (ai, aj)), (m[0] * m[1], m[0] * m[1]))

shapes = {
	"square": gen_elliptical_square,
	"cube": gen_elliptical_cube
}

def gen_elliptical(shape, h, order):
	return shapes[shape](h)
	
m1 = 100
h1 = 1 / (m1 + 1)
m2 = 50
h2 = 1 / (m2 + 1)
A = gen_elliptical("square", (h1, h2), 2)
# print(A)
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

for i in range(m1):
	for j in range(m2):
		if (m1 / 8 < i and 7 * m1 / 8 > i and m2 / 8 < j and m2 / 4 > j) or (m1 / 8 < i and m1 / 4 > i and m2 / 8 < j and 7 * m2 / 8 > j):
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
for i in range(m1):
	pretty_u.append([])
	for j in range(m2):
		pretty_u[i].append(u[i * m2 + j])
		
contour(pretty_u)
show()

		












































