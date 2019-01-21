#Author:Yichen Tao(ytao15)
from tkinter import *
from counterWP import *
from tkinter import messagebox

class CounterGUIWP():
  def __init__(self):
    self.root_window = Tk()
    self.top_frame = Frame(self.root_window)
    self.mid_frame = Frame(self.root_window)
    self.bottom_frame = Frame(self.root_window)
    self.__counter = CounterWP()

    self.count_up_botton = Button(self.top_frame,text = "C O U N T  U P !",command = self.count_up)
    self.count_down_botton = Button(self.top_frame,text = "C O U N T  D O W N !",command = self.count_down)
    self.reset_botton = Button(self.mid_frame, text = " RESET Counter ",command = self.reset)
    self.entry = Entry(self.mid_frame, width = 7)
    self.entry.bind("<Return>", self.set)

    self.prompt = Label(self.mid_frame,text = "Set Counter: ")
    self.label = Label(self.bottom_frame, text = "Count = ")

    self.__i_val = IntVar()
    #checker = self.__counter.get_value()
    self.__i_val.set(self.__counter.get_value())
    self.display_label = Label(self.bottom_frame, textvariable = self.__i_val)

    self.count_up_botton.grid(row = 0, column = 0)
    self.count_down_botton.grid(row = 0, column = 1)
    self.reset_botton.grid(row = 0, column = 0)

    self.prompt.grid(row = 0, column = 1)
    self.entry.grid(row = 0,column = 2)

    self.label.grid(row = 0,column = 0)
    self.display_label.grid(row = 0,column = 1)
    
    self.top_frame.grid(row = 0, column = 0)
    self.mid_frame.grid(row = 1, column = 0)
    self.bottom_frame.grid(row = 2, column = 0)

    self.root_window.mainloop()

  def count_up(self):
    self.__counter.increment()
    self.__i_val.set(self.__counter.get_value())
    #print(self.__i_val)

  def count_down(self):
    if self.__i_val.get()>0:
      self.__counter.decrement()
      self.__i_val.set(self.__counter.get_value())
    else:
      messagebox.showerror("Value Error","Can not count below zero.")
    
  def reset(self):
    self.__counter.reset()
    self.__i_val.set(self.__counter.get_value())

  def set(self,event):
    value_str = self.entry.get()
    value = int(value_str)
    if value >= 0:
      self.__counter.set(str(value))
      self.__i_val.set(self.__counter.get_value())
    else:
      messagebox.showerror("Value Error","Can not enter negative value.")
    self.entry.delete(0,END)
    #######*****----------
    #Did not implement private helper methods due to lack of time.

if __name__ == "__main__":
  test = CounterGUIWP()
  print("x")
