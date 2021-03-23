# Given a sudoku, create a new sudoku from it
import numpy as np
from numpy import genfromtxt
import random

def swap_row(pz:[], rows:tuple):
	row1, row2 = rows
	pz[[row1,row2],:] = pz[[row2,row1],:]

def swap_col(pz:[], cols:tuple):
	col1, col2 = cols
	pz[:,[col1,col2]] = pz[:,[col2,col1]]

def swap_blocks(pz:[], left_right=True):
	if left_right:
		for col in range(3):
			swap_col(pz, (col, col+6))
	else:
		for row in range(3):
			swap_row(pz, (row, row+6))
	
def mirror(pz:[], left_right=True):
	if left_right:
		for col in range(4):
			swap_col(pz, (col, 8-col))
	else:
		for row in range(4):
			swap_row(pz, (row, 8-row))

def rotate(pz:[], k:int):
	pz[:] = np.rot90(pz, k)

def random_remap_numbers(pz:[], l:[]):
	random.shuffle(l)
	print(["{}->{}".format(i+1,l[i]) for i in range(9)])
	for r in pz:
		for i in range(9):
			if r[i] > 0:
				r[i] = l[r[i]-1]

functions = [
(swap_row, (0,2), "swap row 1,3"),
(swap_row, (3,5), "swap row 4,6"),
(swap_row, (6,8), "swap row 7,9"),
(swap_col, (0,2), "swap column 1,3"),
(swap_col, (3,5), "swap column 4,6"),
(swap_col, (6,8), "swap column 7,9"),
(mirror, True, "mirror left right"),
(mirror, False, "mirror top bottom"),
(swap_blocks, True, "swap left right 3 columns"),
(swap_blocks, False, "swap top bottom 3 rows"),
(rotate, 1, "rotate 90 anticlockwise"),
(rotate, 2, "rotate 180"),
(rotate, 3, "rotate 90 clockwise"),
(random_remap_numbers, [1,2,3,4,5,6,7,8,9], "random remap numbers")
]

def main():
	puzzle = genfromtxt('sudoku.csv', delimiter=',', dtype=int)
	print("Read sudoku puzzle from 'sudoku.csv'")
	print(puzzle)
	print()
	
	random.shuffle(functions)
	n = random.randrange(1,len(functions))
	for i in range(n):
		f, p, fctname = functions[i]
		print(fctname)
		f(puzzle, p)
		print(puzzle)
		print()

if __name__ == "__main__":
	main()
