#Author: Yichen Tao

from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from tictactoe import *

class TicTacToeGUI:
  def __init__(self):
    self.__game_new = TicTacToe()
    self.__game_new.set_name_cross_player("No name1")
    self.__game_new.set_name_oval_player("No name2")
    self.__root_window = Tk()
    #self.set_init_gamer()
    self.__set_up_GUI()
    self.set_init_gamer()
    #self.__game_new = TicTacToe()
    #self.__game_new.set_name_cross_player("Need attention")
    self.__root_window.mainloop()

  def __set_up_GUI(self):
    #self.__set_init_gamer()
    #self.set_init_gamer()
    self.__top_name_frame = Frame(self.__root_window)
    self.__middle_name_frame = Frame(self.__root_window)
    self.__bottom_name_frame = Frame(self.__root_window)
    self.__bottom_playing_frame = Frame(self.__root_window)
    self.__bottom_game_board_frame = Frame(self.__root_window)
    #self.__game_new.set_name_cross_player("Need attention")

    self.__cross_player_name_var = StringVar()
    self.__cross_player_name_var.set(self.__game_new.get_name_cross_player())

    self.__oval_player_name_var = StringVar()
    self.__oval_player_name_var.set(self.__game_new.get_name_oval_player())

    self.__initiative_name_var = StringVar()
    self.__initiative_name_var.set("No name1")

    self.__playing_player_name_var = StringVar()
    self.__playing_player_name_var.set("No name1")

    self.__cross_player_label = Label(self.__top_name_frame,text = "Cross : ")
    self.__cross_player_name_label = Label(self.__top_name_frame,textvariable = self.__cross_player_name_var)
    self.__cross_name_set_button = Button(self.__top_name_frame,text = "SET NAME")
    self.__cross_name_set_button['command'] = self.set_name_cross

    self.__oval_player_label = Label(self.__middle_name_frame,text = "Oval : ")
    self.__oval_player_name_label = Label(self.__middle_name_frame,textvariable = self.__oval_player_name_var)
    self.__oval_name_set_button = Button(self.__middle_name_frame,text = "SET NAME")
    self.__oval_name_set_button['command'] = self.set_name_oval

    self.__initiative_player_label = Label(self.__bottom_name_frame,text = "Initiative : ")
    self.__initiative_player_name_label = Label(self.__bottom_name_frame,textvariable = self.__initiative_name_var)
    self.__initiative_name_set_button = Button(self.__bottom_name_frame,text = "SET INITIATIVE")
    self.__initiative_name_set_button['command'] = self.set_init_gamer

    self.__playing_player_label = Label(self.__bottom_playing_frame,text = "PLAYING : ")
    self.__playing_player_name_label = Label(self.__bottom_playing_frame,textvariable = self.__playing_player_name_var)

    canvas_width = 40
    canvas_height = 40
    canvas_bg_1 = "#%02x%02x%02x"%(0,43,54)
    canvas_bg_2 ="#%02x%02x%02x"%(42,161,152)

    self.__top_left = Canvas(self.__bottom_game_board_frame, width=canvas_width, height=canvas_height)
    self.__top_left['bg'] = canvas_bg_1
    self.__top_left.bind("<Button-1>", self.set_top_left)
##    test = self.__top_left.create_oval(33, 33, 10, 10,width = 5,outline = "red")
##    self.__top_left.delete(test)
    self.__top_middle = Canvas(self.__bottom_game_board_frame, width=canvas_width, height=canvas_height)
    self.__top_middle['bg'] = canvas_bg_2
    self.__top_middle.bind("<Button-1>", self.set_top_middle)
    #self.__top_middle.create_line(5,5,38,38,width = 5,fill = 'red')
    #self.__top_middle.create_line(5,38,38,5,width = 5,fill = 'red')
    self.__top_right = Canvas(self.__bottom_game_board_frame, width=canvas_width, height=canvas_height)
    self.__top_right['bg'] = canvas_bg_1
    self.__top_right.bind("<Button-1>", self.set_top_right)
    
    self.__middle_left = Canvas(self.__bottom_game_board_frame, width=canvas_width, height=canvas_height)
    self.__middle_left['bg'] = canvas_bg_2
    self.__middle_left.bind("<Button-1>", self.set_middle_left)
    self.__middle_middle = Canvas(self.__bottom_game_board_frame, width=canvas_width, height=canvas_height)
    self.__middle_middle['bg'] = canvas_bg_1
    self.__middle_middle.bind("<Button-1>", self.set_middle_middle)
    self.__middle_right = Canvas(self.__bottom_game_board_frame, width=canvas_width, height=canvas_height)
    self.__middle_right['bg'] = canvas_bg_2
    self.__middle_right.bind("<Button-1>", self.set_middle_right)
    
    self.__bottom_left = Canvas(self.__bottom_game_board_frame, width=canvas_width, height=canvas_height)
    self.__bottom_left['bg'] = canvas_bg_1
    self.__bottom_left.bind("<Button-1>", self.set_bottom_left)
    self.__bottom_middle = Canvas(self.__bottom_game_board_frame, width=canvas_width, height=canvas_height)
    self.__bottom_middle['bg'] = canvas_bg_2
    self.__bottom_middle.bind("<Button-1>", self.set_bottom_middle)
    self.__bottom_right = Canvas(self.__bottom_game_board_frame, width=canvas_width, height=canvas_height)
    self.__bottom_right['bg'] = canvas_bg_1
    self.__bottom_right.bind("<Button-1>", self.set_bottom_right)


    self.__cross_player_label.grid(row = 2,column = 0)
    self.__cross_player_name_label.grid(row = 2,column = 1)
    self.__cross_name_set_button.grid(row = 2, column = 2)

    self.__oval_player_label.grid(row = 2,column = 0)
    self.__oval_player_name_label.grid(row = 2,column = 1)
    self.__oval_name_set_button.grid(row = 2, column = 2)

    self.__initiative_player_label.grid(row = 2,column = 0)
    self.__initiative_player_name_label.grid(row = 2,column = 1)
    self.__initiative_name_set_button.grid(row = 2, column = 2)

    self.__playing_player_label.grid(row = 2,column = 0)
    self.__playing_player_name_label.grid(row = 2,column = 1)

    self.__top_left.grid(row = 0, column =0)
    self.__top_middle.grid(row = 0, column =1)
    self.__top_right.grid(row = 0, column =2)

    self.__middle_left.grid(row = 1, column =0)
    self.__middle_middle.grid(row = 1, column =1)
    self.__middle_right.grid(row = 1, column =2)

    self.__bottom_left.grid(row = 2, column =0)
    self.__bottom_middle.grid(row = 2, column =1)
    self.__bottom_right.grid(row = 2, column =2)

    self.__top_name_frame.pack()
    self.__middle_name_frame.pack()
    self.__bottom_name_frame.pack()
    self.__bottom_playing_frame.pack()
    self.__bottom_game_board_frame.pack()

  def set_top_left(self,event):
    #print("KKKKKKKKKK")
    #print()
    board_now = self.__game_new.get_game_board()
    if not board_now[0]:
      #print("Empty")
      if self.__playing_player_name_var.get() == self.__game_new.get_name_cross_player():
        #print("OOOOOO")
        top_left_line1 = self.__top_left.create_line(5,5,38,38,width = 5,fill = 'red')
        top_left_line2 = self.__top_left.create_line(5,38,38,5,width = 5,fill = 'red')
        #print("PPPPPPPPPPPPPPP")
      else:
        top_left_oval = self.__top_left.create_oval(33, 33, 10, 10,width = 5,outline = "red")
      self.__game_new.play_game(0)
      player = self.__game_new.get_inner_count()
      if player == 0:
        self.__playing_player_name_var.set(self.__game_new.get_initiative_player())
      else:
        #print("step1")
        if self.__game_new.get_initiative_player() == self.__game_new.get_name_cross_player():
          print("step2")
          self.__playing_player_name_var.set(self.__game_new.get_name_oval_player())
        else:
          #print("step3")
          self.__playing_player_name_var.set(self.__game_new.get_name_cross_player())
      results = self.__game_new.check_game_status()
      if results[0]:
        if results[1] == self.__game_new.CROSS:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_cross_player()+" is the winner!")
        else:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_oval_player()+" is the winner!")
        self.reset()
      #print(str(self.__game_new))
      elif self.check_if_tie(board_now):
        messagebox.showinfo("Congratulations","Game is over, no one is the winner")
        self.reset()

  def set_top_middle(self,event):
    board_now = self.__game_new.get_game_board()
    if not board_now[1]:
      #print("KKKKKKKKKK")
      #print()
      if self.__playing_player_name_var.get() == self.__game_new.get_name_cross_player():
        #print("OOOOOO")
        top_middle_line1 = self.__top_middle.create_line(5,5,38,38,width = 5,fill = 'red')
        top_middle_line2 = self.__top_middle.create_line(5,38,38,5,width = 5,fill = 'red')
        #print("PPPPPPPPPPPPPPP")
      else:
        top_middle_oval = self.__top_middle.create_oval(33, 33, 10, 10,width = 5,outline = "red")
      self.__game_new.play_game(1)
      player = self.__game_new.get_inner_count()
      if player == 0:
        self.__playing_player_name_var.set(self.__game_new.get_initiative_player())
      else:
        if self.__game_new.get_initiative_player() == self.__game_new.get_name_cross_player():
          self.__playing_player_name_var.set(self.__game_new.get_name_oval_player())
        else:
          self.__playing_player_name_var.set(self.__game_new.get_name_cross_player())
      results = self.__game_new.check_game_status()
      if results[0]:
        if results[1] == self.__game_new.CROSS:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_cross_player()+" is the winner!")
        else:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_oval_player()+" is the winner!")
        self.reset()
      #print(str(self.__game_new))
      elif self.check_if_tie(board_now):
        messagebox.showinfo("Congratulations","Game is over, no one is the winner")
        self.reset()

  def set_top_right(self,event):
    board_now = self.__game_new.get_game_board()
    if not board_now[2]:
      #print("KKKKKKKKKK")
      #print()
      if self.__playing_player_name_var.get() == self.__game_new.get_name_cross_player():
        #print("OOOOOO")
        top_right_line1 = self.__top_right.create_line(5,5,38,38,width = 5,fill = 'red')
        top_right_line2 = self.__top_right.create_line(5,38,38,5,width = 5,fill = 'red')
        #print("PPPPPPPPPPPPPPP")
      else:
        top_right_oval = self.__top_right.create_oval(33, 33, 10, 10,width = 5,outline = "red")
      self.__game_new.play_game(2)
      player = self.__game_new.get_inner_count()
      if player == 0:
        self.__playing_player_name_var.set(self.__game_new.get_initiative_player())
      else:
        if self.__game_new.get_initiative_player() == self.__game_new.get_name_cross_player():
          self.__playing_player_name_var.set(self.__game_new.get_name_oval_player())
        else:
          self.__playing_player_name_var.set(self.__game_new.get_name_cross_player())
      results = self.__game_new.check_game_status()
      if results[0]:
        if results[1] == self.__game_new.CROSS:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_cross_player()+" is the winner!")
        else:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_oval_player()+" is the winner!")
        self.reset()
      #print(str(self.__game_new))
      elif self.check_if_tie(board_now):
        messagebox.showinfo("Congratulations","Game is over, no one is the winner")
        self.reset()

  def set_middle_left(self,event):
    board_now = self.__game_new.get_game_board()
    if not board_now[3]:
      #print("KKKKKKKKKK")
      #print()
      if self.__playing_player_name_var.get() == self.__game_new.get_name_cross_player():
        #print("OOOOOO")
        middle_left_line1 = self.__middle_left.create_line(5,5,38,38,width = 5,fill = 'red')
        middle_left_line2 = self.__middle_left.create_line(5,38,38,5,width = 5,fill = 'red')
        #print("PPPPPPPPPPPPPPP")
      else:
        middle_left_oval = self.__middle_left.create_oval(33, 33, 10, 10,width = 5,outline = "red")
      self.__game_new.play_game(3)
      player = self.__game_new.get_inner_count()
      if player == 0:
        self.__playing_player_name_var.set(self.__game_new.get_initiative_player())
      else:
        if self.__game_new.get_initiative_player() == self.__game_new.get_name_cross_player():
          self.__playing_player_name_var.set(self.__game_new.get_name_oval_player())
        else:
          self.__playing_player_name_var.set(self.__game_new.get_name_cross_player())
      results = self.__game_new.check_game_status()
      if results[0]:
        if results[1] == self.__game_new.CROSS:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_cross_player()+" is the winner!")
        else:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_oval_player()+" is the winner!")
        self.reset()
      #print(str(self.__game_new))
      elif self.check_if_tie(board_now):
        messagebox.showinfo("Congratulations","Game is over, no one is the winner")
        self.reset()

  def set_middle_middle(self,event):
    board_now = self.__game_new.get_game_board()
    if not board_now[4]:
      #print("KKKKKKKKKK")
      #print()
      if self.__playing_player_name_var.get() == self.__game_new.get_name_cross_player():
        #print("OOOOOO")
        middle_middle_line1 = self.__middle_middle.create_line(5,5,38,38,width = 5,fill = 'red')
        middle_middle_line2 = self.__middle_middle.create_line(5,38,38,5,width = 5,fill = 'red')
        #print("PPPPPPPPPPPPPPP")
      else:
        middle_middle_oval = self.__middle_middle.create_oval(33, 33, 10, 10,width = 5,outline = "red")
      self.__game_new.play_game(4)
      player = self.__game_new.get_inner_count()
      if player == 0:
        self.__playing_player_name_var.set(self.__game_new.get_initiative_player())
      else:
        if self.__game_new.get_initiative_player() == self.__game_new.get_name_cross_player():
          self.__playing_player_name_var.set(self.__game_new.get_name_oval_player())
        else:
          self.__playing_player_name_var.set(self.__game_new.get_name_cross_player())
      results = self.__game_new.check_game_status()
      if results[0]:
        if results[1] == self.__game_new.CROSS:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_cross_player()+" is the winner!")
        else:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_oval_player()+" is the winner!")
        self.reset()
      #print(str(self.__game_new))
      elif self.check_if_tie(board_now):
        messagebox.showinfo("Congratulations","Game is over, no one is the winner")
        self.reset()

  def set_middle_right(self,event):
    board_now = self.__game_new.get_game_board()
    if not board_now[5]:
      #print("KKKKKKKKKK")
      #print()
      if self.__playing_player_name_var.get() == self.__game_new.get_name_cross_player():
        #print("OOOOOO")
        middle_right_line1 = self.__middle_right.create_line(5,5,38,38,width = 5,fill = 'red')
        middle_right_line2 = self.__middle_right.create_line(5,38,38,5,width = 5,fill = 'red')
        #print("PPPPPPPPPPPPPPP")
      else:
        middle_right_oval = self.__middle_right.create_oval(33, 33, 10, 10,width = 5,outline = "red")
      self.__game_new.play_game(5)
      player = self.__game_new.get_inner_count()
      if player == 0:
        self.__playing_player_name_var.set(self.__game_new.get_initiative_player())
      else:
        if self.__game_new.get_initiative_player() == self.__game_new.get_name_cross_player():
          self.__playing_player_name_var.set(self.__game_new.get_name_oval_player())
        else:
          self.__playing_player_name_var.set(self.__game_new.get_name_cross_player())
      results = self.__game_new.check_game_status()
      if results[0]:
        if results[1] == self.__game_new.CROSS:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_cross_player()+" is the winner!")
        else:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_oval_player()+" is the winner!")
        self.reset()
      #print(str(self.__game_new))
      elif self.check_if_tie(board_now):
        messagebox.showinfo("Congratulations","Game is over, no one is the winner")
        self.reset()

  def set_bottom_left(self,event):
    board_now = self.__game_new.get_game_board()
    if not board_now[6]:
      #print("KKKKKKKKKK")
      #print()
      if self.__playing_player_name_var.get() == self.__game_new.get_name_cross_player():
        #print("OOOOOO")
        bottom_left_line1 = self.__bottom_left.create_line(5,5,38,38,width = 5,fill = 'red')
        bottom_left_line2 = self.__bottom_left.create_line(5,38,38,5,width = 5,fill = 'red')
        #print("PPPPPPPPPPPPPPP")
      else:
        bottom_left_oval = self.__bottom_left.create_oval(33, 33, 10, 10,width = 5,outline = "red")
      self.__game_new.play_game(6)
      player = self.__game_new.get_inner_count()
      if player == 0:
        self.__playing_player_name_var.set(self.__game_new.get_initiative_player())
      else:
        if self.__game_new.get_initiative_player() == self.__game_new.get_name_cross_player():
          self.__playing_player_name_var.set(self.__game_new.get_name_oval_player())
        else:
          self.__playing_player_name_var.set(self.__game_new.get_name_cross_player())
      results = self.__game_new.check_game_status()
      if results[0]:
        if results[1] == self.__game_new.CROSS:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_cross_player()+" is the winner!")
        else:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_oval_player()+" is the winner!")
        self.reset()
      #print(str(self.__game_new))
      elif self.check_if_tie(board_now):
        messagebox.showinfo("Congratulations","Game is over, no one is the winner")
        self.reset()

  def set_bottom_middle(self,event):
    board_now = self.__game_new.get_game_board()
    if not board_now[7]:
      #print("KKKKKKKKKK")
      #print()
      if self.__playing_player_name_var.get() == self.__game_new.get_name_cross_player():
        #print("OOOOOO")
        bottom_middle_line1 = self.__bottom_middle.create_line(5,5,38,38,width = 5,fill = 'red')
        bottom_middle_line2 = self.__bottom_middle.create_line(5,38,38,5,width = 5,fill = 'red')
        #print("PPPPPPPPPPPPPPP")
      else:
        bottom_middle_oval = self.__bottom_middle.create_oval(33, 33, 10, 10,width = 5,outline = "red")
      self.__game_new.play_game(7)
      player = self.__game_new.get_inner_count()
      if player == 0:
        self.__playing_player_name_var.set(self.__game_new.get_initiative_player())
      else:
        if self.__game_new.get_initiative_player() == self.__game_new.get_name_cross_player():
          self.__playing_player_name_var.set(self.__game_new.get_name_oval_player())
        else:
          self.__playing_player_name_var.set(self.__game_new.get_name_cross_player())
      results = self.__game_new.check_game_status()
      if results[0]:
        if results[1] == self.__game_new.CROSS:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_cross_player()+" is the winner!")
        else:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_oval_player()+" is the winner!")
        self.reset()
      #print(str(self.__game_new))
      elif self.check_if_tie(board_now):
        messagebox.showinfo("Congratulations","Game is over, no one is the winner")
        self.reset()

  def set_bottom_right(self,event):
    board_now = self.__game_new.get_game_board()
    if not board_now[8]:
      #print("KKKKKKKKKK")
      #print()
      if self.__playing_player_name_var.get() == self.__game_new.get_name_cross_player():
        #print("OOOOOO")
        bottom_right_line1 = self.__bottom_right.create_line(5,5,38,38,width = 5,fill = 'red')
        bottom_right_line2 = self.__bottom_right.create_line(5,38,38,5,width = 5,fill = 'red')
        #print("PPPPPPPPPPPPPPP")
      else:
        bottom_right_oval = self.__bottom_right.create_oval(33, 33, 10, 10,width = 5,outline = "red")
      self.__game_new.play_game(8)
      player = self.__game_new.get_inner_count()
      if player == 0:
        self.__playing_player_name_var.set(self.__game_new.get_initiative_player())
      else:
        if self.__game_new.get_initiative_player() == self.__game_new.get_name_cross_player():
          self.__playing_player_name_var.set(self.__game_new.get_name_oval_player())
        else:
          self.__playing_player_name_var.set(self.__game_new.get_name_cross_player())
      results = self.__game_new.check_game_status()
      if results[0]:
        if results[1] == self.__game_new.CROSS:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_cross_player()+" is the winner!")
        else:
          messagebox.showinfo("Congratulations",self.__game_new.get_name_oval_player()+" is the winner!")
        self.reset()
      #print(str(self.__game_new))
      elif self.check_if_tie(board_now):
        messagebox.showinfo("Congratulations","Game is over, no one is the winner")
        self.reset()

  def set_init_gamer(self):
    self.__game_new.set_initiative_player()
    self.__initiative_name_var.set(self.__game_new.get_initiative_player())
    player = self.__game_new.get_inner_count()
    if player == 0:
      self.__playing_player_name_var.set(self.__game_new.get_initiative_player())
    else:
      if self.__game_new.get_initiative_player() == self.__game_new.get_name_cross_player():
        self.__playing_player_name_var.set(self.__game_new.get_name_oval_player())
      else:
        self.__playing_player_name_var.set(self.__game_new.get_name_cross_player())

  def check_if_tie(self,game_board):
    count = 0
    for item in game_board:
      if item:
        count+=1
    if count == 9:
        answer = True
    else:
        answer = False
    return answer

  def set_name_cross(self):
    cross_name = simpledialog.askstring("Enter name","Enter name of people using cross.",parent = self.__root_window)
    if not (cross_name == self.__game_new.get_name_oval_player()):
      self.__game_new.set_name_cross_player(cross_name)
      self.__cross_player_name_var.set(self.__game_new.get_name_cross_player())
    else:
      messagebox.showerror("Error","Do not input same names.")

  def reset(self):
    self.__game_new.reset()
    self.__top_left.delete(ALL)
    self.__top_middle.delete(ALL)
    self.__top_right.delete(ALL)
    
    self.__middle_left.delete(ALL)
    self.__middle_middle.delete(ALL)
    self.__middle_right.delete(ALL)
    
    self.__bottom_left.delete(ALL)
    self.__bottom_middle.delete(ALL)
    self.__bottom_right.delete(ALL)

  def set_name_oval(self):
    oval_name = simpledialog.askstring("Enter name","Enter name of people using oval.",parent = self.__root_window)
    if not (oval_name == self.__game_new.get_name_cross_player()):
      self.__game_new.set_name_oval_player(oval_name)
      self.__oval_player_name_var.set(self.__game_new.get_name_oval_player())
    else:
      messagebox.showerror("Error","Do not input same names.")
    

if __name__ == "__main__":
  TicTacToeGUI()
