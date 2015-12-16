from board import Board, string_to_list

def get_peers(board, r, c): #get the lists of used values for row, col, box
	cols = board.col_peers[c]
	rows = board.row_peers[r]
	box_number = (r / 3) * 3 + (c / 3)
	boxs = board.box_peers[box_number]
	return cols, rows, boxs

def or_peers(l1, l2, l3):
	return list(set(l1) | set(l2) | set(l3))
	
#returns the row of the empty slot in a column
def empty_spot(board, c):
	for i in range(0, 9):
		if board.board[c + 9 * i] == 0:
			return i
	return 0
	
def col_eval(board, c):
	cell_peers = [] #initialize list of lists of values for each cell in column

	for r in range(0, 9):
		cell_val = board.get_cell_val(r, c)
		if cell_val != 0:
			cell_peers.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
		else:
			x, y, z = get_peers(board, r, c)
			orps = or_peers(x, y, z)
			# print c, r, x, y, z
			# print orps
			cell_peers.append(orps)
			# print "r: ", r, orps
			if len(cell_peers[r]) == 8: #if there's already one option, fills it.
				row = empty_spot(board, c)
				# print "there were 8 peers", cell_peers[r]
				board.add_val((set(cell_peers[r]) ^ 
							set([1, 2, 3, 4, 5, 6, 7, 8, 9])).pop(),r, c)
				return 1
			
	for v in range(1,10):
		miss_count = 0
		miss_index = -1
		for n in range(0,9):
			if cell_peers[n].count(v) == 1:
				continue
			else:
				miss_count+= 1
				miss_index = n
				if miss_count > 1:
					break
		if miss_count == 1:
			board.add_val(v, miss_index, c)
			# print "miss count was one"
			return 1
	#print cell_peers
	
def row_eval(board, r):
	cell_peers = [] #list of values for each cell in given row
	
	for c in range(0,9):
		cell_val = board.get_cell_val(r, c)
		if cell_val != 0:
			cell_peers.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
		else: 
			x, y, z = get_peers(board, r, c)
			orps = or_peers(x, y, z)
			# print c, r, x, y, z
			# print orps
			cell_peers.append(orps)
			# print "r: ", r, orps
			if len(cell_peers[c]) == 8: #if there's already one option, fills it.
				row = empty_spot(board, c)
				# print "there were 8 peers", cell_peers[r]
				board.add_val((set(cell_peers[c]) ^ 
							set([1, 2, 3, 4, 5, 6, 7, 8, 9])).pop(),r, c)
				return 1
				
	for v in range(1,10):
		miss_count = 0
		miss_index = -1
		for n in range(0,9):
			if cell_peers[n].count(v) == 1:
				continue
			else:
				miss_count+= 1
				miss_index = n
				if miss_count > 1:
					break
		if miss_count == 1:
			board.add_val(v, r, miss_index)
			# print "miss count was one", v
			return 1
	
	
def solve_step(board):
	for i in range(0, 9):
		worked = col_eval(board, i)
		if worked == 1:
			print "COL:"
			board.print_board()
			return 0
			break
	for j in range(0,9):
		worked = row_eval(board, j)
		if worked == 1:
			print "ROW:"
			board.print_board()
			return 0
			break
		
	return 1
	
def solve_board(board):
	board.parse_board()
	board.print_board()
	is_done = 0
	while is_done == 0:
		is_done = solve_step(board)
	board.print_board()
	print board.empties
	return board.board
			
def main():
	test_board = """
	. 2 9 1 . . . . .
	. . 1 . 8 . . . . 
	. . 4 6 . 2 . . . 
	7 6 . . 9 1 . 8 .
	4 . . . . . . . 9
	. 9 . 2 3 . . 1 4
	. . . 5 . 8 3 . .
	. . . . 2 . 9 . . 
	. . . . . 6 5 4 ."""
	board_list = string_to_list(test_board)
	testing = Board(board_list)
	solve_board(testing)

	
main()

	
