chess_board = [[-1, -1, -1, -1, -1, -1, -1, -1,-1] for n in range(9)]
moves = [(2, 1), (2, -1), (-2, -1), (-2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())


queue = [[x1, y1, 0]]

def on_board(x, y):
  return 0 < x < 9 and 0 < y < 9

def BFS(queue,chess_board):
  for n in queue:
    if n[0] == x2 and n[1] == y2:
      return n[2]
    for dx,dy in moves:
      newstep = n[2] + 1
      newx = n[0] + dx
      newy = n[1] + dy
      if on_board(newx, newy) == True and chess_board[newy][newx] == -1:
        chess_board[newy][newx] = (newstep)

        queue.append([newx,newy,newstep])

print(BFS(queue,chess_board))


"""
if on_board(newx, newy) == True and chess_board[newy][newx] == -1:
                chess_board[newy][newx] = newstep
                queue.append([newx, newy, newstep])
                """
