#Author: Yichen Tao
from librarymodule import *
from library import *
from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
import os
class FileHandleGui:
  LOAD_FILE = "0"
  NEW_FILE = "1"
  FILE_TYPE = [('binary file', '.*')]
  def __init__(self):
    self.__root_window = Tk()
    self.__root_window['bg'] = "#%02x%02x%02x"%(0,43,54)

    self.__choice_value_first = StringVar()
    self.__choice_value_first.set(self.NEW_FILE)
    self.__load_file_button = Radiobutton(self.__root_window,text = "Load file",\
                                        variable = self.__choice_value_first, value = self.LOAD_FILE)
    self.__load_file_button['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__load_file_button['bg'] = "#%02x%02x%02x"%(0,43,54)
    self.__new_file_button = Radiobutton(self.__root_window,text = "New file",\
                                         variable = self.__choice_value_first, value = self.NEW_FILE)
    self.__new_file_button['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__new_file_button['bg'] = "#%02x%02x%02x"%(0,43,54)
    #print(self.__choice_value_first.get())
    self.__continue_botton = Button(self.__root_window,text = "Continue",\
                                    command = self.__first_choice_handler)
    self.__continue_botton['fg'] = "#%02x%02x%02x"%(42,161,152)
    self.__continue_botton['bg'] = "#%02x%02x%02x"%(0,43,54)

    self.__load_file_button.pack()
    self.__new_file_button.pack()
    self.__continue_botton.pack()
    
    self.__root_window.mainloop()

    #print(self.__choice_value_first.get())

  def __first_choice_handler(self):
    #print(self.__choice_value_first.get())
    if self.__choice_value_first.get() == self.LOAD_FILE:
      #print("True")
      self.__file_name = filedialog.askopenfilename(parent = self.__root_window,\
                                                    initialdir=os.getcwd(),\
                                                    title="Please select the file to load.",\
                                                    filetypes=self.FILE_TYPE)
##      if os.path.sep not in self.__file_name:
##        self.__file_name.replace("//",os.path.sep)
##        self.__file_name.replace("\\\\",os.path.sep)
##        self.__file_name.replace("/",os.path.sep)
##        self.__file_name.replace("\\",os.path.sep)
##        print("Change")
##        print(os.path.sep)
        
      #print(self.__file_name)
      self.__library_object_record = LibraryRecords(self.__file_name)
      self.__library_object = self.__library_object_record.load()
    else:
      #print("False")
      self.__file_dir = filedialog.askdirectory(parent = self.__root_window,\
                                                initialdir=os.getcwd(),\
                                                title = "Please select the directory to save new record.")
      #print(self.__file_dir)
      self.__new_file_name = simpledialog.askstring("Name of new record.",\
                                                    "Please input name for new record file.",\
                                                    parent = self.__root_window)
      if not self.__new_file_name:
        self.__new_file_name = "new_library_record"
      self.__file_name = os.path.join(self.__file_dir,self.__new_file_name)
      self.__library_object_record = LibraryRecords(self.__file_name)
      self.__library_name_temp = simpledialog.askstring("Name of library",\
                                                      "Please input name of the library.",\
                                                      parent = self.__root_window)
      #print(self.__library_name_temp)
      self.__library_object = Library(self.__library_name_temp)
      self.__library_object.set_name(self.__library_name_temp)
      #print(self.__library_object.get_name())
      #print(__library_name_temp)

      #print(self.__file_name)
    self.__root_window.destroy()
  def save_record(self):
    self.__library_object_record.save(self.__library_object)

  def get_library(self):
    return self.__library_object


if __name__ == "__main__":
  FileHandleGui()
  libraryre = LibraryRecords("file1")
  test =libraryre.load()
  print(str(test))
  #print(FileHandleGui.__choice_value_first.get())
