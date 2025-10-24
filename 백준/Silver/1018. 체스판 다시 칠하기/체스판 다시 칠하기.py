import sys

N, M = [int(n) for n in sys.stdin.readline().split()]
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

min_painting = 64

for sr in range(N-7):
	for sc in range(M-7):
		count_start_W = 0
		count_start_B = 0
		for r in range(sr, sr+8):
			for c in range(sc, sc+8):
				if r % 2 == 0:
					if c % 2 == 0:
						if board[r][c] == "B":
							count_start_W += 1
						if board[r][c] == "W":
							count_start_B += 1
					else:
						if board[r][c] == "W":
							count_start_W += 1
						if board[r][c] == "B":
							count_start_B += 1
				else:
					if c % 2 == 0:
						if board[r][c] == "W":
							count_start_W += 1
						if board[r][c] == "B":
							count_start_B += 1
					else:
						if board[r][c] == "B":
							count_start_W += 1
						if board[r][c] == "W":
							count_start_B += 1

		result = min(count_start_B,count_start_W)
		if result < min_painting:
			min_painting = result

print(min_painting)