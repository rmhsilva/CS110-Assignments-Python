#Author : Yichen Tao
import random

class TicTacToe:
  OVAL = "o"
  CROSS = "x"
  def __init__(self):
    self.__cross_player_name = ""
    self.__oval_player_name = ""
    self.__game_board = GameBoard()
    self.__initiative_player = ""
    self.__inner_count = 0

  def check_game_status(self):
    return self.__game_board.did_anyone_win()

  def play_game(self,position):
    if self.__inner_count == 0:
      self.__inner_count+=1
      #print("KKKKKKKKKK")
      if self.__initiative_player == self.__cross_player_name:
        self.__game_board.set_board(position,self.CROSS)
      elif self.__initiative_player == self.__oval_player_name:
        self.__game_board.set_board(position,self.OVAL)
    elif self.__inner_count ==1:
      self.__inner_count-=1
      #print("PPPPPPPPPPPP")
      if self.__initiative_player == self.__cross_player_name:
        self.__game_board.set_board(position,self.OVAL)
      elif self.__initiative_player == self.__oval_player_name:
        self.__game_board.set_board(position,self.CROSS)

  def get_inner_count(self):
    #print(self.__inner_count)
    return self.__inner_count

  def get_initiative_player(self):
    return self.__initiative_player

  def set_initiative_player(self):
    self.__initiative_player = random.choice((self.__cross_player_name,self.__oval_player_name))

  def set_name_cross_player(self,name):
    self.__cross_player_name = name

  def set_name_oval_player(self,name):
    self.__oval_player_name = name

  def reset(self):
    self.__game_board.reset()

  def get_name_cross_player(self):
    return self.__cross_player_name

  def get_name_oval_player(self):
    return self.__oval_player_name

  def get_game_board(self):
    new_board = self.__game_board.get_board()
    return new_board

  def __str__(self):
    out_str = "Cross (x): %s\nOval (o) : %s\n"%(self.__cross_player_name,self.__oval_player_name)
    out_str+=str(self.__game_board)
    return out_str

class GameBoard:
  TOP_LEFT = 0
  TOP_MIDDLE = 1
  TOP_RIGHT = 2

  MIDDLE_LEFT = 3
  MIDDLE_MIDDLE = 4
  MIDDLE_RIGHT = 5

  BOTTOM_LEFT = 6
  BOTTOM_MIDDLE = 7
  BOTTOM_RIGHT = 8
  
  def __init__(self):
    self.__board = [None,None,None,
                    None,None,None,
                    None,None,None]

  def reset(self):
    self.__board = [None,None,None,
                    None,None,None,
                    None,None,None]

  def did_anyone_win(self):
    win_or_not = False
    first_check_symbol = self.__board[self.TOP_LEFT]#1
    second_check_symbol = self.__board[self.TOP_MIDDLE]#2
    third_check_symbol = self.__board[self.TOP_RIGHT]#3
    fourth_check_symbol = self.__board[self.MIDDLE_LEFT]#4
    fifth_check_symbol = self.__board[self.BOTTOM_LEFT]#5
    winner = ""

    if first_check_symbol and ((first_check_symbol == self.__board[self.TOP_MIDDLE] and first_check_symbol == self.__board[self.TOP_RIGHT]) or\
       (first_check_symbol == self.__board[self.MIDDLE_MIDDLE] and first_check_symbol == self.__board[self.BOTTOM_RIGHT]) or\
       (first_check_symbol == self.__board[self.MIDDLE_LEFT] and first_check_symbol == self.__board[self.BOTTOM_LEFT])):
      win_or_not = True
      winner = first_check_symbol
    elif second_check_symbol and ((second_check_symbol == self.__board[self.MIDDLE_MIDDLE] and second_check_symbol == self.__board[self.BOTTOM_MIDDLE])):
      win_or_not = True
      winner = second_check_symbol
    elif third_check_symbol and ((third_check_symbol == self.__board[self.MIDDLE_MIDDLE] and third_check_symbol == self.__board[self.BOTTOM_LEFT]) or\
         (third_check_symbol == self.__board[self.MIDDLE_RIGHT] and third_check_symbol == self.__board[self.BOTTOM_RIGHT])):
      win_or_not = True
      winner = third_check_symbol
    elif fourth_check_symbol and (fourth_check_symbol == self.__board[self.MIDDLE_MIDDLE] and fourth_check_symbol == self.__board[self.MIDDLE_RIGHT]):
      win_or_not = True
      winner = fourth_check_symbol
    elif fifth_check_symbol and (fifth_check_symbol == self.__board[self.BOTTOM_MIDDLE] and fifth_check_symbol == self.__board[self.BOTTOM_RIGHT]):
      win_or_not = True
      winner = fifth_check_symbol
    return (win_or_not,winner if winner else None)

  def set_board(self,position,player_symbol):
    if not self.__board[position]:
      self.__board[position] = player_symbol

  def get_board(self):
    return self.__board

  def __str__(self):
    board_out_str = "%s|%s|%s\n"%(str(self.__board[self.TOP_LEFT]).center(5),str(self.__board[self.TOP_MIDDLE]).center(5),str(self.__board[self.TOP_RIGHT]).center(5))
    board_out_str += "-"*18+"\n"
    board_out_str += "%s|%s|%s\n"%(str(self.__board[self.MIDDLE_LEFT]).center(5),str(self.__board[self.MIDDLE_MIDDLE]).center(5),str(self.__board[self.MIDDLE_RIGHT]).center(5))
    board_out_str += "-"*18+"\n"
    board_out_str += "%s|%s|%s\n"%(str(self.__board[self.BOTTOM_LEFT]).center(5),str(self.__board[self.BOTTOM_MIDDLE]).center(5),str(self.__board[self.BOTTOM_RIGHT]).center(5))
    return board_out_str

if __name__ == "__main__":
##  print("k")
##  board = GameBoard()
##  print(board)
##  board.set_board(0,"x")
##  board.set_board(4,"x")
##  board.set_board(8,"x")
##  print(board)
##  print(board.did_anyone_win())
  game = TicTacToe()
  game.set_name_cross_player("Charles")
  game.set_name_oval_player("Anna")
  print(game)
  game.set_initiative_player()
  print(game.get_initiative_player())
  game.play_game(0)
  game.play_game(1)
  game.play_game(1)
  game.play_game(4)
  game.play_game(2)
  game.play_game(8)
  print(game)
  print(game.check_game_status())
  print(game.get_game_board())
