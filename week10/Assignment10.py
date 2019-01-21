
'''
TAO YICHEN
ytao15@binghamton.edu
Assignment10
Lab section: B56
CA name: Paul Maino
Assignment #10 Part 1
Phone: 6079532749
'''
"""
Write a program that repeatedly encrypts or decrypts a message given the
operation to perform and either the rotation key (when encrypting) or the
rotation key that was used to encrypt (in the case of decrypting)

Output to monitor:
  new_message (str)

Input from keyboard:
  message (str)
  operation (str) - 'E', 'e', 'D', or 'd'
  rotation_key(int)

Tasks allocated to functions:
  validate_operation() - simple Predicate function
  validate_rotation_key() - simple Predicate function
  convert_rotation_key()
  keep_in_bounds()
  process_message()
"""

#For file validation
import os.path

#Initialize constants ---------------------------------------------------------

# Required file extension
FILE_EXT = ".txt"

# File processing modes
READ_MODE = 'r'
WRITE_MODE = 'w'

#Available operations
OPERATIONS = {'e':(1,"Encrypted"), 'd':(-1,"Decrypted")}

# Min and limit ordinals of printable ASCII
PRINTABLE_ASCII_MIN = 32
PRINTABLE_ASCII_LIMIT = 127
ONE = 1
# Allowable rotation key prefixes
KEY_PREFIX = "-"

# Functions ------------------------------------------------------------------

#-------------make_name--------------
#  Generates output file name from input file name, operation requested
#    and converted rotation key
# param file_name (str)
# param operation (str)
# param rotation_key (int) - converted key
# invoke  str.split(), str.replace()  and str.join()
# return output file name (str)
def make_name (file_name, operation, rotation_key):
  name_list = file_name.split(".")
  name_list[0] = name_list [0] .replace(OPERATIONS['e'][1], "")
  name_list[0] = name_list [0] .replace(OPERATIONS['d'][1], "")
  name_list[0] += (OPERATIONS[operation][1] + str(rotation_key))
  return ".".join(name_list)

#-------------process_message_list-------------------------
# Processes list of lines (i.e.,mesages) from input file list
#   one line at a time
# param new_list (list)
# param rotation_key (int)
# invoke list.append()
#        process_message()
# return list of precessed lines (i.e.,messages) (list)
def process_message_list(new_list, rotation_key):
  new_line_list = []
  for old_line in new_list:
    new_line = process_message(old_line,rotation_key)
    new_line_list.append(new_line)
  #new_line_list = [process_message(old_line,rotation_key) for old_line in new_list]
  return new_line_list

#------------validate_file_name-------------
#  You only need to use this if you haven't finished
#    implementing your exception handling
#    Once your exception handling is in place, comment his out & its usage
#  Checks that file exists and that extension is .txt
# param name (str)
# invoke isifle() from module os.path and endswith()
# return True when valid, False otherwise (bool)
def validate_file_name(name):
  return os.path.isfile(name) and name.endswith(FILE_EXT)

#------------write_to_file---------------
#  You may have noticed that this violaes our style guideline,
#    but for this program, it will keep your code more streamlined
#    So do it this way until you get the hang of exception handling
#    Note: the exception handling will be in the caller, not here
# Write each line in output list to file
# param file (type: _io.TextIOWrapper - i.e., it's a text file)
# param text_list (list)
# return None
def write_to_file (file,text_list):
 out_text_list = [in_line+"\n" for in_line in text_list]
 #print(out_text_list)
## for out in out_text_list:
##   file.write(out)
 file.writelines(out_text_list)
 file.close()

# Check that requested operation is valid
# param op_str (str) - operation requested
# invoke len()
# invoke str.lower()
# return  True when valid, False otherwise (bool)
def validate_operation(op_str): #Used
  return op_str.lower() in OPERATIONS

# Check that rotation key is of form <digits> or -<digits>
# param rotation_key_str (str)
# invoke str.isdigit() 
# returns:  True when valid, False otherwise (bool)
def validate_rotation_key(rotation_key_str): #Used
  comparator = rotation_key_str.replace(KEY_PREFIX,'')
  negative_count = rotation_key_str.count(KEY_PREFIX)
  return ((negative_count <= ONE and comparator.isdigit()) and int(comparator) !=0)

# Convert rotation key to value usable for requested operation
# param  op (str) - operation requested 
# param  rotation_key_str (str)
# invoke int()
# return encryption or decryption rotation key (int)
def convert_rotation_key(op_str, rotation_key_str):#used
  return (int(rotation_key_str)*(OPERATIONS['e'][0]))\
        if op_str.lower() == 'e'\
        else (int(rotation_key_str)*(OPERATIONS['d'][0]))

# Perform string modulus operation to prevent processed character 
# from going out of bounds
# param ordinal (int)
# returns adjusted ordinal of new character (int)
# Hint:  Use two sequential while loops
def keep_in_bounds(ordinal):#used
  while ordinal >= PRINTABLE_ASCII_LIMIT:
    ordinal -= (PRINTABLE_ASCII_LIMIT-PRINTABLE_ASCII_MIN)
  while ordinal < PRINTABLE_ASCII_MIN:
    ordinal += (PRINTABLE_ASCII_LIMIT-PRINTABLE_ASCII_MIN)
  return ordinal

# Encrypt or decrypt message using rotation_key
# param message (str)
# param rotation_key (int)
# invoke keep_in_bounds() 
# return processed_message (str)
def process_message(message, rotation_key):
  message_out = ''
  character_new = ''
  for character in message:
    character_new = chr(keep_in_bounds(ord(character)+rotation_key))
    message_out += character_new
    #print(character)
    #print(message_out)
  return message_out

# Main -----------------------------------------------------------------------

# Gets plain text or cipher code, operation requested (encrypt or decrypt),
#   and rotation key for Caesar cipher
# Generates cipher code or plain text
def main():
  # Describe program
  print("This program encrypts or decrypts messages " + \
        "using a Caesar cipher")

  # Priming read and repeat
##  message = input("What is your message?\n"
##                  "Press <Enter to quit.\n")

  #Enhance your Ceasar cipher program to
  #allow a user to repeatedly specify
  #an entire file of plain text or
  #encrypted text to process
  #Have them input the file name (instead of a line of text)
  #the requested operation
  #and the rotation key
  file_name = input("What is the file you want to process?\n"
                    "Press <Enter> to quit.\n")
##  while message:
  while file_name:
    # Get remaining inputs, validate and convert as necessary  
    operation = input("Do you want to encrypt(e) or decrypt(d)?\n")
    while not validate_operation(operation):
      print("Invalid input!\n")
      operation = input("Do you want to encrypt(e) or decrypt(d)?\n")
    rotation_key_str = input("What is the rotation key?\n")
    while not validate_rotation_key(rotation_key_str):
      print("Invalid input!\n")
      rotation_key_str = input("What is the rotation key?\n")
    rotation_key = convert_rotation_key(operation, rotation_key_str)
    
    # Encrypt or decrypt contents of message
    try:
      outFileObject = open(file_name,READ_MODE)

      try:
        content_in = outFileObject.readlines()
        content_list = [line.replace("\n","") for line in content_in]
        content_processed = process_message_list(content_list, rotation_key)

        try:
          name_output = make_name (file_name, operation, rotation_key)
          inFileObject = open(name_output,WRITE_MODE)

          try:
            write_to_file (inFileObject,content_processed)
          except IOError as err:
            print("\nProblem writing data: \n" + str(err))
          except ValueError as err:
            print("\nProblem writing data, wrong format or corrupted?  \n" + str(err) + '\n')
          except Exception as err:
            print("\nData cannot be written to file: \n" + str(err) + '\n')
          finally:
            inFileObject.close()

        except IOError as err:
          print("\nExecption raised during open of output file, no write performed: \n" + str(err) + '\n')
        except Exception as err:
          print("\nData cannot be read:  \n" + str(err) + '\n')
          
      except IOError as err:
        print("\nProblem reading data: \n" + str(err))
      except ValueError as err:
        print("\nProblem processing data, wrong format or corrupted? \n" + str(err) + '\n')
      except Exception as err:
        print("\nData cannot be read:  \n" + str(err) + '\n')
      finally:
        outFileObject.close()

    except FileNotFoundError as err:
      print("\nFile not found:  deleted or in wrong folder?  \n" + str(err) + '\n')
    except IOError as err:
      print("\nException raised during open of input file, try a different file: \n" + str(err) + '\n')
    except Exception as err:
      print("\nData cannot be read:  \n" + str(err) + '\n')
      

##    message_out = process_message(message, rotation_key)

##    # Display result
##    print("This is the new message.")
##    print(message_out)


    # Continuation read
##    message = input("\n\nWhat is your message?\n"
##                  "Press <Enter to quit.\n")
    file_name = input("What is the file you want to process?\n"
                        "Press <Enter> to quit.\n")
main()
