import itertools



class Board:
	def __init__(self):
		self.board = ['' for i in range(9)]

	def _check(self,it):
		q = 0
		for k in itertools.combinations(it,2):
			if self.board[k[0]] == '' or self.board[k[1]] == '':continue
			if self.board[k[0]] == self.board[k[1]]:q += 1
			if q==3:return self.board[i]

	def check(self):
		''' 
		Return winner's sign
		'''
		n = 0
		for i in range(9):
			if self.board[i] != '':n += 1
			if n==9:return "draw"
		for i in range(3):
			self._check(range(3*i,3*i+3))
			self._check(range(i,i+7,3))
		if self.board[4] != '':
			self._check([0,4,8])
			self._check([2,4,6])
		return 0

	def __str__(self):
		s = ''
		for i in range(3):
			s += ' '.join(self.board[3*i:3*i+3])
			s += '\n'
		return s

class Player:
	def __init__(self,board,sign):
		self.board = board
		self.sign = sign

	def move(self, pos):
		if self.board.board[pos] == '':self.board.board[pos] = self.sign
		else:return -1
		return 0