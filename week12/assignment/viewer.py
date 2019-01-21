#Author: Yichen Tao
from tkinter import *
from tkinter import messagebox
import os
from book import *
from library import *
from librarymodule import *
from patron import *
from storage import *
#The viewer part is finished.
#Author: Yichen Tao
#Have not connected to model and controller yet.
class LibraryGUI:
  def __init__(self):
    self.__FileHandler = FileHandleGui()
    self.__LibraryObject = self.__FileHandler.get_library()
##    print("123------------------")
##    print(LibraryObject)
##    print("456--------------------")
    #LibraryViewObject = LibraryGUI()
##    print(LibraryViewObject.s_library.get())
    #print("test")
    self.__root_window = Tk()
    self.__set_up_gui()
  def __set_up_gui(self):#viewer
    #The whole program uses dark polarized theme as my color choice
    #The number usage is non linear and based on the project outline
    #So the numbers may not follow a continuous sequence
    self.__root_window['bg'] = "#%02x%02x%02x"%(0,43,54)

    #---------Text of the title bar-----------------------------
    self.__file_dir_path = os.path.dirname(os.path.realpath(__file__))
    self.__root_window.title(self.__file_dir_path)#Set title of the window.

    #--------Frames-----------------------------------
    self.__name_library_frame = Frame(self.__root_window)#First_line : Library_name
    self.__name_library_frame['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__title_book_frame = Frame(self.__root_window)#Second_line : Book_title
    #self.__title_book_frame['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__title_book_frame['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__author_book_frame = Frame(self.__root_window)#Third_line : Book_author
    self.__author_book_frame['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__patron_book_frame = Frame(self.__root_window)#Fourth_line : Book_patron
    self.__patron_book_frame['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__status_frame = Frame(self.__root_window)#Fifth_line : Status
    self.__status_frame['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__patron_name_frame = Frame(self.__root_window)#Sixth_line : Patron name or empty string
    self.__patron_name_frame['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__author_name_frame= Frame(self.__root_window)#Seventh_line : Author name or empty string
    self.__author_name_frame['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__book_first_buttons_frame= Frame(self.__root_window)#Eighth_line : Check_out_botton and Return_botton
    self.__book_first_buttons_frame['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__search_group_buttons_frame = Frame(self.__root_window)#Tenth_line : Search_book_botton and Search_patron_botton
    self.__search_group_buttons_frame['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__patron_membership_group_buttons_frame = Frame(self.__root_window)#Twelveth_line : Patron_join_botton and Patron_leave_botton
    self.__patron_membership_group_buttons_frame['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__book_membership_group_buttons_frame = Frame(self.__root_window)#Fourteenth_line : Book_add_botton and Book_remove_botton
    self.__book_membership_group_buttons_frame['bg'] = "#%02x%02x%02x"%(0,43,54)

    #-------First_line_parameter--------------------
    self.s_library = StringVar()
    self.s_library.set("Name of Library")
    self.s_library.set(self.__LibraryObject.get_name())
    self.title_text = Label(self.__name_library_frame, textvariable = self.s_library)
    self.title_text['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.title_text['bg'] = "#%02x%02x%02x"%(0,43,54)

    #------Second_line_parameter---------------
##    self.__check_out_lable = Label(self.__title_book_frame, text = "Check Out Books")
##    self.__check_out_lable['fg'] = "#%02x%02x%02x"%(42,161,152)
##    self.__check_out_lable['bg'] = "#%02x%02x%02x"%(0,43,54)
##    self.__return_label = Label(self.__title_book_frame, text = "Return Books")
##    self.__return_label['fg'] = "#%02x%02x%02x"%(42,161,152)
##    self.__return_label['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__title_first_2 = Label(self.__title_book_frame, text = "Book Title: ")
    self.__title_first_2['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__title_first_2['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__title_first_2_entry = Entry(self.__title_book_frame)
##    self.__title_second_2 = Label(self.__title_book_frame, text = "Title:")
##    self.__title_second_2['fg'] = "#%02x%02x%02x"%(42,161,152)
##    self.__title_second_2['bg'] = "#%02x%02x%02x"%(0,43,54)
##    self.__title_second_2_entry = Entry(self.__title_book_frame)

    #--------Third_line_parameter-----------
    self.__author_name_3 = Label(self.__author_book_frame, text = "Book Author: ")
    self.__author_name_3['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__author_name_3['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__author_name_3_entry = Entry(self.__author_book_frame)

    #-------Fourth_line_parameter------------
    self.__patron_name_4 = Label(self.__patron_book_frame, text = "Book Patron: ")
    self.__patron_name_4['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__patron_name_4['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__patron_name_4_entry = Entry(self.__patron_book_frame)

    #-------Fifth_line_parameter-------------
    self.__status_first_label_5 = Label(self.__status_frame, text = "Status: ")
    self.__status_first_label_5['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__status_first_label_5['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__status = StringVar()
    self.__status.set("Need attention")
    self.__status.set(self.__LibraryObject.get_transaction_status())
    self.__status_second_label_5 = Label(self.__status_frame, textvariable = self.__status)
    self.__status_second_label_5['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__status_second_label_5['bg'] = "#%02x%02x%02x"%(0,43,54)

    #---------Sixth_line_parameter----------
    self.__patron_first_label_6 = Label(self.__patron_name_frame, text = "Patron: ")
    self.__patron_first_label_6['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__patron_first_label_6['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__patron_name = StringVar()
    self.__patron_name.set("")
    self.__patron_second_label_6 = Label(self.__patron_name_frame, textvariable = self.__patron_name)
    self.__patron_second_label_6['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__patron_second_label_6['bg'] = "#%02x%02x%02x"%(0,43,54)

    #--------Seventh_line_parameter-------------
    self.__author_name_first_label_7 = Label(self.__author_name_frame, text = "Author: ")
    self.__author_name_first_label_7['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__author_name_first_label_7['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__author_name = StringVar()
    self.__author_name.set("")
    self.__author_name_second_label_7 = Label(self.__author_name_frame, textvariable = self.__author_name)
    self.__author_name_second_label_7['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__author_name_second_label_7['bg'] = "#%02x%02x%02x"%(0,43,54)

    #--------Eighth_line_parameter--------------
    self.__book_op_first_label_8 = Label(self.__book_first_buttons_frame, text = "Book: ")
    self.__book_op_first_label_8['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__book_op_first_label_8['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__book_checkout_button_8 = Button(self.__book_first_buttons_frame, text = "Check Out book.")
    self.__book_checkout_button_8['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__book_checkout_button_8['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__book_checkout_button_8['command'] = self.__check_out_book
    self.__book_return_button_8 = Button(self.__book_first_buttons_frame, text = "Return Book.")
    self.__book_return_button_8['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__book_return_button_8['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__book_return_button_8['command'] = self.__return_book

    #-------Tenth_line_parameter---------------
    self.__search_op_label_10 = Label(self.__search_group_buttons_frame, text = "Search: ")
    self.__search_op_label_10['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__search_op_label_10['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__search_book_button_10 = Button(self.__search_group_buttons_frame, text = "Search book.")
    self.__search_book_button_10['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__search_book_button_10['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__search_book_button_10['command'] = self.__search_book
    self.__search_patron_button_10 = Button(self.__search_group_buttons_frame, text = "Search patron.")
    self.__search_patron_button_10['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__search_patron_button_10['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__search_patron_button_10['command'] = self.__search_patron

    #--------Twelveth_line_parameter--------------
    self.__membership_op_label_12 = Label(self.__patron_membership_group_buttons_frame, text = "Patron membership: ")
    self.__membership_op_label_12['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__membership_op_label_12['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__membership_join_patron_button_12 = Button(self.__patron_membership_group_buttons_frame, text = "Patron join.")
    self.__membership_join_patron_button_12['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__membership_join_patron_button_12['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__membership_join_patron_button_12['command'] = self.__add_patron
    self.__membership_leave_patron_button_12 = Button(self.__patron_membership_group_buttons_frame, text = "Patron leave.")
    self.__membership_leave_patron_button_12['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__membership_leave_patron_button_12['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__membership_leave_patron_button_12['command'] = self.__remove_patron

    #--------Fourteenth_line_parameter--------------
    self.__book_membership_op_label_14 = Label(self.__book_membership_group_buttons_frame, text = "Book: ")
    self.__book_membership_op_label_14['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__book_membership_op_label_14['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__membership_add_book_button_14 = Button(self.__book_membership_group_buttons_frame, text = "Add book.")
    self.__membership_add_book_button_14['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__membership_add_book_button_14['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__membership_add_book_button_14['command'] = self.__add_book
    self.__membership_remove_book_button_14 = Button(self.__book_membership_group_buttons_frame, text = "Remove book.")
    self.__membership_remove_book_button_14['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__membership_remove_book_button_14['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__membership_remove_book_button_14['command'] = self.__remove_book
    self.__quit_button = Button(self.__book_membership_group_buttons_frame, text="Save and quit.")
    self.__quit_button['command'] = self.__quit_op
    self.__quit_button['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__quit_button['bg'] = "#%02x%02x%02x"%(0,43,54)

    #--------Line_Show_Grid--------------
    self.title_text.grid()
##    self.__check_out_lable.grid(row = 0, column = 1,padx = 120)#"Check Out Books"
##    self.__return_label.grid(row = 0, column = 3,padx = 100)#"Return Books"
    self.__title_first_2.grid(row = 2,column = 0)
    self.__title_first_2_entry.grid(row = 2,column = 1)
    self.__author_name_3.grid(row = 2, column = 0)
    self.__author_name_3_entry.grid(row = 2,column = 1)
    self.__patron_name_4.grid(row = 2,column = 0)
    self.__patron_name_4_entry.grid(row = 2, column = 1)
    self.__status_first_label_5.grid(row = 2, column = 0)
    self.__status_second_label_5.grid(row = 2, column = 1)
    self.__patron_first_label_6.grid(row = 2, column = 0)
    self.__patron_second_label_6.grid(row = 2,column = 1)
    self.__author_name_first_label_7.grid(row = 2, column = 0)
    self.__author_name_second_label_7.grid(row = 2,column = 1)#Next line is 8
    self.__book_op_first_label_8.grid(row = 2, column = 0)
    self.__book_checkout_button_8.grid(row = 2, column = 1)
    self.__book_return_button_8.grid(row = 3,column = 1)#Next line is 10
    self.__search_op_label_10.grid(row = 2, column = 0)
    self.__search_book_button_10.grid(row = 2, column = 1)
    self.__search_patron_button_10.grid(row = 3,column = 1)#next line is 12
    self.__membership_op_label_12.grid(row = 2, column = 0)
    self.__membership_join_patron_button_12.grid(row = 2, column = 1)
    self.__membership_leave_patron_button_12.grid(row = 3,column = 1)#next line is 14
    self.__book_membership_op_label_14.grid(row = 2, column = 0)
    self.__membership_add_book_button_14.grid(row = 2, column = 1)
    self.__membership_remove_book_button_14.grid(row = 3,column = 1)#next line is 14
    self.__quit_button.grid(row = 4,column = 1, sticky = E+W,pady = 10,padx = 20)

##    self.__title_second_2.grid(row = 2,column = 2)
##    self.__title_second_2_entry.grid(row =2,column =3)
##    self.title_text.grid()
##    self.__check_out_lable.pack()
##    self.__return_label.pack()
##    self.__title_first_2.pack()
##    self.__title_first_2_entry.pack()
##    self.__title_second_2.pack()
##    self.__title_second_2_entry.pack()

    #-------Frame_Show_Pack----------------
    self.__name_library_frame.pack()#1
    self.__title_book_frame.pack()#2
    self.__author_book_frame.pack()#3
    self.__patron_book_frame.pack()#4
    self.__status_frame.pack()#5
    self.__patron_name_frame.pack()#6
    self.__author_name_frame.pack()#7
    self.__book_first_buttons_frame.pack()#8
    self.__search_group_buttons_frame.pack()#10
    self.__patron_membership_group_buttons_frame.pack()#12
    self.__book_membership_group_buttons_frame.pack()#14

    #self.__name_library_frame.grid(row = 1,column = 1,padx = 45)
    #self.__name_library_frame.grid()

    self.__root_window.mainloop()

  def __quit_op(self):
    #print("asdf")
    self.__root_window.destroy()
    self.__FileHandler.save_record()

  def __remove_book(self):
    book_name = self.__title_first_2_entry.get()
    if book_name:
      self.__LibraryObject.remove_book(book_name)
      self.__status.set(self.__LibraryObject.get_transaction_status())
      self.__title_first_2_entry.delete(0,END)
    else:
      messagebox.showerror("Lack Info","Input book name.")

  def __add_book(self):
    book_name = self.__title_first_2_entry.get()
    book_author = self.__author_name_3_entry.get()
    if book_name and book_author:
      BookObject = Book(book_name,book_author)
      self.__LibraryObject.add_book(BookObject)
      self.__status.set(self.__LibraryObject.get_transaction_status())
      self.__title_first_2_entry.delete(0,END)
      self.__author_name_3_entry.delete(0,END)
    else:
      messagebox.showerror("Lack Info","Input book name and author.")

  def __remove_patron(self):
    book_name = self.__title_first_2_entry.get()
    if patron_name:
      self.__LibraryObject.remove_patron(patron_name)
      self.__status.set(self.__LibraryObject.get_transaction_status())
      self.__patron_name_4_entry.delete(0,END)
    else:
      messagebox.showerror("Lack Info","Input patron name.")

  def __add_patron(self):
    patron_name = self.__patron_name_4_entry.get()
    if patron_name:
      PatronObject = Patron(patron_name)
      self.__LibraryObject.add_patron(PatronObject)
      self.__status.set(self.__LibraryObject.get_transaction_status())
      self.__patron_name_4_entry.delete(0,END)
    else:
      messagebox.showerror("Lack Info","Input patron name.")

  def __search_patron(self):
    patron_name = self.__patron_name_4_entry.get()
    if patron_name:
      PatronObject = self.__LibraryObject.get_patron(patron_name)
      if PatronObject:
        self.__status.set(str(PatronObject)+"\n"+self.__LibraryObject.get_transaction_status())
        self.__patron_name_4_entry.delete(0,END)
    else:
      messagebox.showerror("Lack Info","Input patron name.")

  def __search_book(self):
    book_name = self.__title_first_2_entry.get()
    if book_name:
      BookObject = self.__LibraryObject.get_book(book_name)
      if BookObject:
        self.__status.set(str(BookObject)+"\n"+self.__LibraryObject.get_transaction_status())
        self.__title_first_2_entry.delete(0,END)
    else:
      messagebox.showerror("Lack Info","Input book name.")

  def __return_book(self):
    book_name = self.__title_first_2_entry.get()
    if book_name:
      BookObject = self.__LibraryObject.get_book(book_name)
      if BookObject:
        BookObject.return_me()
        self.__status.set(BookObject.get_transaction_status())
        self.__title_first_2_entry.delete(0,END)
    else:
      messagebox.showerror("Lack Info","Input book name.")

  def __check_out_book(self):
    book_name = self.__title_first_2_entry.get()
    patron_name = self.__patron_name_4_entry.get()
    if book_name and patron_name:
      BookObject = self.__LibraryObject.get_book(book_name)
      PatronObject = self.__LibraryObject.get_patron(patron_name)
      if BookObject and PatronObject:
        BookObject.borrow_me(PatronObject)
        self.__status.set(BookObject.get_transaction_status())
        #print("kkkkkkkkkkkkk")
        self.__title_first_2_entry.delete(0,END)
        self.__patron_name_4_entry.delete(0,END)
    else:
      messagebox.showerror("Lack Info","Input both book name and patron name.")

if __name__ == "__main__":
  LibraryGUI()
