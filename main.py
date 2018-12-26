from game import *

def get_coord():
	flag = True
	while flag:
		coords = list(map(int, input("Your move (x,y): ").split()))
		flag = False
		if coords[0] == 0 or coords[1] == 0 or coords[0]>8 or coords[1]>8:flag=True
	return 3*(coords[0]-1) + coords[1] - 1

def plr_move(player):
	flag = True
	while flag:
		pos  = get_coord()
		s = player.move(pos)
		flag = False
		if s == -1:
			print("Try again!")
			flag = True
	
def main():
	board = Board()
	plr = Player(board,'X')
	enemey = Player(board, 'O') 
	i = 0	
	while i<9:
		print(board)
		plr_move(plr)
		result = board.check()
		if result == "draw":break
		elif result != 0:
			print("Winner is %s" % result)
			break
		print(board)
		plr_move(enemey)
		result = board.check()
		if result == "draw":break
		elif result != 0:
			print("Winner is %s" % result)
			break


		
if __name__ == '__main__':
	main()