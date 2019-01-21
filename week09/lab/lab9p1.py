'''
TAO YICHEN
ytao15@binghamton.edu
Lab9
Lab section: B56
CA: Paul Maino
Lab9,Part1
Phone: 6079532749
'''
#-----------------Part1
a = [1, 2, 3]
b = a[:]
b[0] = 5
print(a)
print(b)
print("id of a: %d\nid of %db\n"%(id(a),id(b)))
answer = a is b
print("a is b:",answer)
print("id of second character of a and b: %d %d\n"%(id(a[1]),id(b[1])))
answer = a[1] is b[1]
print("a is b:",answer)

#-------------------Part2
myList=[]
myList[len(myList):] =[76]
myList[len(myList):] =[92.3]
myList[len(myList):] =["hello"]
myList[len(myList):] =[True]
myList[len(myList):] =[4]
myList[len(myList):] =[76]
print(myList)

#------------------Part3
#a. Append “apple” and 76 to the list.
myList[len(myList):] =["apple",76]
print(myList)
#b. Insert the value “cat” at position 3
myList.insert(3,"cat")
print(myList)
#c. Insert the value 99 at the start of the list.
myList[0] = 99
myList.insert(0,99)
print(myList)
#d. Find the index of “hello”.
index = myList.index("hello")
print(index)
#e. Count the number of 76s in the list.
print(myList.count("hello"))
#f. Remove the first occurrence of 76 from the list.
myList.remove("hello")
print(myList)
#g. Remove True from the list using pop and index.
myList.pop(myList.index(True))
print(myList)
