class Board(object):

	def __init__(self, init_list):
		self.board = init_list
		self.col_peers = []
		self.row_peers = []
		self.box_peers = []
		self.empties = []

	
	#prints a copy of the board readable to user
	def print_board(self):
		list_with_dots = self.board
		list_with_dots = [x if (x!=0) else '.' for x in list_with_dots]
		print """
.----------------------.
| {} {} {} | {} {} {} | {} {} {}|
| {} {} {} | {} {} {} | {} {} {}|
| {} {} {} | {} {} {} | {} {} {}|
|-------|-------|------|
| {} {} {} | {} {} {} | {} {} {}|
| {} {} {} | {} {} {} | {} {} {}|
| {} {} {} | {} {} {} | {} {} {}|
|-------|-------|------|
| {} {} {} | {} {} {} | {} {} {}|
| {} {} {} | {} {} {} | {} {} {}|
| {} {} {} | {} {} {} | {} {} {}|
'----------------------'
		""".format(*list_with_dots)
		
	#adds or changes a value on the board
	#can be used with 0 to make a space blank
	def add_val(self, val, row, col):
		self.board[9 * row + col] = val
		self.col_peers[col].append(val)
		self.row_peers[row].append(val)
		box_number = (row / 3) * 3 + (col / 3)
		self.box_peers[box_number].append(val)
	
	def remove_val(self, row, col):
		self.board[9 * row + col] = 0
		

	#creates the col, row, and box peers lists
	def parse_cols(self):
		#for a column i, the ith list in the list will 
		#contain which numbers are set in the col
		for i in range(0, 9): #loop across cols
			values_in_col = []
			
			for j in range(0, 9): #loop down rows
				box_index = j*9 + i
				x = self.board[box_index]
				if x:
					values_in_col.append(x) #create list of peers in col
			self.col_peers.append(values_in_col) #append to list of all cols
		
	def parse_rows(self):
		#for a row i, the the ith list in the list will
		#contain which numbers are set in the row
		for j in range(0, 9): #loop down rows
			values_in_row = []
			for i in range(0, 9): #loop across cols
				x = self.board[j*9 + i]
				if x != 0:
					values_in_row.append(x) #create list of peers in row
			
			self.row_peers.append(values_in_row) #append to list of all rows
	
	def parse_boxes(self):
		#for a box i, the ith list in the list will
		#contain which numbers are set in the box
		#boxes are 1-9 left to right, & top to bottom
		for b in range(0,9): #loop over boxes
			start_row = (b / 3) * 3 
			start_col = (b % 3) * 3
			
			values_in_box = []
			for i in range (0, 3): #loop across cols in box
				for j in range (0, 3): #loop across rows in box
					r = start_row + j
					c = start_col + i
					x = self.board[r*9 + c]
					if x != 0:
						values_in_box.append(x)
			
			self.box_peers.append(values_in_box)
			
	def parse_board(self):
		self.parse_rows()
		self.parse_cols()
		self.parse_boxes()
		
		#print self.row_peers
		#print self.col_peers
		#print self.box_peers
	
	def get_cell_val(self, row, col):
		return self.board[row*9 + col]
		

def string_to_list(string_input):
	board_list = [0]*81

	#separating each relevant character of string
	list_of_vals = list(string_input)
		
	#removing the separators from the list
	separators = ['\n', '\t', ' ']
	list_of_vals = [x for x in list_of_vals 
							if x not in separators]
	
	#assigning the values to correct index on board
	#blank spaces treated as 0
	for i in range (0, 81):
		val = list_of_vals[i]
		num = 0
		if val != '.':
			num = int(val)
		board_list[i] = num	
		
	return board_list
	
def main():		
	test_board = Board("""
	. 2 9 1 . . . . .
	. . 1 . 8 . . . . 
	. . 4 6 . 2 . . . 
	7 6 . . 9 1 . 8 .
	4 . . . . . . . 9
	. 9 . 2 3 . . 1 4
	. . . 5 . 8 3 . .
	. . . . 2 . 9 . . 
	. . . . . 6 5 4 .""")
	#test_board.print_board()
	#test_board.add_val(6, 0, 7)
	#test_board.print_board()
	#test_board.remove_val(0, 7)
	#test_board.print_board()
	
main()
	
