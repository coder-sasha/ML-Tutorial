"""
some tricks with matrices.
observe two things:
 - use f-string to concatenate strings;
 - the pythonic way to swap variables;
"""

def swap_diagonal(m: list[list[int]]) -> None: 
	n = len(m) 
	for i in range(n): 
		t = m[i][i] 
		m[i][i] = m[i][n-i-1] 
		m[i][n-i-1] = t 


def transpose(m: list[list[int]]) -> None: 
	x = len(m) 
	y = len(m[0]) 
	
	for i in range(x): 
		for j in range(i, y): 
			# tuple unpacking - the more pythonic swap than in swap-diagonal() :)
			m[j][i], m[i][j] = m[i][j], m[j][i]


def print_mx(m: list[list[int]]) -> str: 
	r = "-----------\n" 
	for i in range(len(m)): 
		for j in range(len(m[i])): 
			r = f"{r} {str(m[i][j])} " 
		r = f"{r}\n" 

	return r 

# transpose a matrix. 
mx1 = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 2, 3], [4, 5, 6, 7] ] 
print("The initial matrix is:")
print(print_mx(mx1))
transpose(mx1) 
print("After transposing:")
print(print_mx(mx1))

# swap around a diagonal of matrix.
mx2 = [ [3, 1, 2], [1, 0, 1], [2, 1, 3] ] 
print("The initial matrix is:")
print(print_mx(mx2))
swap_diagonal(mx2) 
print("After diagonal swap:")
print(print_mx(mx2))

