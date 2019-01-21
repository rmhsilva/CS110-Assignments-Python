
'''
TAO YICHEN
ytao15@binghamton.edu
Assignment8
Lab section: B56
CA name: Paul Maino
Assignment #8 Part 1
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


#Initialize constants ---------------------------------------------------------

OPERATIONS = {'e':(1,"Encrypted"), 'd':(-1,"Decrypted")}

# Min and limit ordinals of printable ASCII
PRINTABLE_ASCII_MIN = 32
PRINTABLE_ASCII_LIMIT = 127
ONE = 1
# Allowable rotation key prefixes
KEY_PREFIX = "-"

# Functions ------------------------------------------------------------------

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
  message = input("What is your message?\n"
                  "Press <Enter to quit.\n")
  while message:
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
    message_out = process_message(message, rotation_key)

    # Display result
    print("This is the new message.")
    print(message_out)


    # Continuation read
    message = input("\n\nWhat is your message?\n"
                  "Press <Enter to quit.\n")

main()
