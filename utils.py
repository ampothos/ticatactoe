import random

def main():
  players = ['x', 'o']
  board = {1: ' ',
           2: ' ', 
           3: ' ', 
           4: ' ', 
           5: ' ', 
           6: ' ', 
           7: ' ', 
           8: ' ', 
           9: ' '}
  print('Welcome to 2 player Tic Tac Toe! \nOne player is x, and one player is o.\n')
  if choosePlay():
    bot = players[0]
    human = players[1]
    print(f"The computer is playing as {bot}.")
    for i in board:
      if i % 2 == 0:
        humanMove(human, board)
        cur = human 
      else:
        computerMove(board, bot, human)
        cur = bot
      check = isWinner(board)
      if check:
        print(f'Player {cur.upper()} wins!')
        break
      else:
        check = isDraw(board)
        if check:
          print("It's a draw!")
          break
      
  else:
    turns = random.randint(0,1)
    print(f'{players[turns]} will go first.')

    printBoard(board)
    for i in board:
      current = players[turns%2]
      humanMove(current, board)
      check = isWinner(board)

      if check:
        print(f'Player {current.upper()} wins!')
        break
      else:
        check = isDraw(board)
        if check:
          print("It's a draw!")
          break
      turns += 1

def choosePlay():
  """takes yes or no user input, returns true if bot play, false if 2 player"""
  choice = input("If you would like to play against the computer, type \"yes\". Otherwise, type \"no\".\n").lower()
  while choice != "yes" and choice != "no":
    choice = input("That was not a yes or no. Try again!")
  if choice == "yes":
    return True
  else:
    return False

def printBoard(board):
  horiz = '-------------'
  print(horiz)
  print(f'| {board[7]} | {board[8]} | {board[9]} |')
  print(horiz)
  print(f'| {board[4]} | {board[5]} | {board[6]} |')
  print(horiz)
  print(f'| {board[1]} | {board[2]} | {board[3]} |')
  print(horiz)

def isWinner(b):
  """b: dict board 
  returns true if current is winner, false if not, to continue."""
  if b[1] == b[2] == b[3] and b[1] != ' ': 
    return True
  elif b[4] == b[5] == b[6] and b[4] != ' ': 
    return True
  elif b[7] == b[8] == b[9] and b[7] != ' ': 
    return True
  elif b[1] == b[4] == b[7] and b[1] != ' ': 
    return True
  elif b[2] == b[5] == b[8] and b[2] != ' ': 
    return True
  elif b[3] == b[6] == b[9] and b[3] != ' ':
    return True
  elif b[1] == b[5] == b[9] and b[1] != ' ':
    return True
  elif b[3] == b[5] == b[7] and b[3] != ' ':
    return True
  else: 
    return False

def whichWon(b, mark):
  if b[1] == b[2] == b[3] and b[1] == mark: 
    return True
  elif b[4] == b[5] == b[6] and b[4] == mark: 
    return True
  elif b[7] == b[8] == b[9] and b[7] == mark: 
    return True
  elif b[1] == b[4] == b[7] and b[1] == mark: 
    return True
  elif b[2] == b[5] == b[8] and b[2] == mark: 
    return True
  elif b[3] == b[6] == b[9] and b[3] == mark:
    return True
  elif b[1] == b[5] == b[9] and b[1] == mark:
    return True
  elif b[3] == b[5] == b[7] and b[3] == mark:
    return True
  else: 
    return False

def isDraw(b):
  """b: dict board"""
  for i in b: 
    if b[i] == ' ':
      return False
  return True
  

def humanMove(current, board):
  """current: string letter x or o"""
  pick = int(input(f"Player {current.upper()}, choose your position from numbers 1-9.\n"))
  if pick not in range(1, 10):
    while pick not in range(1, 10):
      pick = int(input("That was not a number 1-9. Try again!"))
  elif board[pick] != ' ':
    while board[pick] != ' ':
      pick = int(input("This spot is already filled, choose a different spot!"))
  board[pick] = current
  printBoard(board)

def computerMove(board, bot, human):
  idealscore = -1000
  idealmove = 0

  for key in board:
    if board[key] == ' ':
      board[key] = bot
      score = minimax(board, False, bot, human)
      board[key] = ' '
      if score > idealscore:
        idealscore = score
        idealmove = key
  
  board[idealmove] = bot
  print("Computer move:")
  printBoard(board)


def minimax(board, isMaximizing, bot, human):
  """board: dict board
  isMaximizing: boolean"""
  # terminal states - reports that either the bot won (good+++) or the human won (bad---)
  if whichWon(board, bot):
    return 100
  elif whichWon(board, human):
    return -100
  elif isDraw(board):
    return 0

# for each possible position, find the best possible score again 
# until the terminal state is reached (winning) - take turns by alternating true and false
# computer player
  if isMaximizing:
    idealscore = -1000
    for key in board:
      if board[key] == ' ':
        board[key] = bot
        score = minimax(board, False, bot, human)
        board[key] = ' '
        if score > idealscore:
          idealscore = score
        
    return idealscore

  # enemy bot
  else:
    idealscore = 1000
    for key in board:
      if board[key] == ' ':
        board[key] = human 
        score = minimax(board, True, bot, human)
        board[key] = ' '
        if score < idealscore:
          idealscore = score
    return idealscore
