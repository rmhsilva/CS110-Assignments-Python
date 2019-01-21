#This file is completed by partner work for lab 10 part 1 and 2
#Author Mathew K Baldwin
#Author Yichen Tao
#partI
#readlines()
def main1():
  myFile = open('rainfall.txt','r')
  accumulator = 0
  myFileList = myFile.readlines()
  minimum = 100
  maximum = 0
  for lst in myFileList:
    temperatureList = lst.split()
    temperature = float(temperatureList[1])
    if temperature < minimum:
      minimum = temperature
    if temperature > maximum:
      maximum = temperature
    accumulator += temperature
  lstAverage = accumulator / len(myFileList)
  print('average =',lstAverage,',minimum =',minimum,',maximum =', maximum)    
main1()

#forloop
def main2():
  myFile = open('rainfall.txt','r')
  accumulator = 0
  accu = 0
  for lst in myFile:
    accu += 1
    temperatureList = lst.split()  
    accumulator += float(temperatureList[1])
  lstAverage = accumulator / accu
  print(lstAverage)
main2()

#readline()
def main3():
  myFile = open('rainfall.txt','r')
  accu = 0
  tempaccumulator = 0
  minimum = 100
  maximum = 0
  temperature = 0
  
  line = myFile.readline()
  while line:
    print(line)
    
    line_list = line.split()
    print(line_list[1])
    temp = float(line_list[1])
    
    if temp < minimum:
      minimum = temp
    if temp > maximum:
      maximum = temp
    tempaccumulator += temp
    accu += 1
    
    line = myFile.readline()
    
  averageTemp = tempaccumulator / accu
  print('average =',averageTemp,',minimum =',minimum,',maximum =', maximum)
    
  
#read()  
def main4():
  accu = 0
  tempaccumulator = 0
  minimum = 100
  maximum = 0
  temperature = 0
  myFile = open('rainfall.txt','r')
  temp_acc = -0
  giant_string = myFile.read()
  giant_list = giant_string.split("\n")
  
  for line in giant_list:
    if line:
    
      line_list = line.split()
      temp = float(line_list[1])
    
      if temp < minimum:
        minimum = temp
      if temp > maximum:
        maximum = temp
      tempaccumulator += temp
      accu += 1
      
    else:
      break
    
  averageTemp = tempaccumulator / accu
  print('average =',averageTemp,',minimum =',minimum,',maximum =', maximum)   
main4()

#partII
def main5():
  myFile = open('conversion.txt','w')
  myFile.write('Fahrenheit    Celcius\n')
  for i in range(-300,213):
    tempF = i
    tempC = (5/9)*(i-32)
    myFile.write('%10.2f %10.2f\n' % (tempF, tempC))
  myFile.close()
  myFile = open('conversion.txt','r')
main5()
