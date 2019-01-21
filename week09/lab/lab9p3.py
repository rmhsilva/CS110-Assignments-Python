def add_fruit(inventory, fruit, quantity=0):
    inventory[fruit] = quantity

# make these tests work...
new_inventory = {}
add_fruit(new_inventory, 'strawberries', 10)
#  test that 'strawberries' in new_inventory
answer = 'strawberries' in new_inventory
print("'strawberries' in new_inventory",answer)
#  test that new_inventory['strawberries'] is 10
answer = new_inventory['strawberries']
answer = (answer == 10)
print("test that new_inventory['strawberries'] is 10",answer)
add_fruit(new_inventory, 'strawberries', 25)
#  test that new_inventory['strawberries'] is now 35)
answer = new_inventory['strawberries']
answer = (answer == 35)
print("test that new_inventory['strawberries'] is 35",answer)
