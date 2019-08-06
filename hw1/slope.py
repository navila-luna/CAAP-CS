# 4 Slope.. but really average  program to sum a series of numbers entered by the user.  basically use an if and tell whether its true or not 
def slope(): 
  print ("Hello! This is a average conversion app. ") 
  total = int(eval(input("How many numbers do you want to average ")))
  numbers = 0 
  for x in range (total): 
    number = int(eval(input("Type next number: ")))
    numbers+= number 
    average = numbers/total 
  print(average) 
  slope ()