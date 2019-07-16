Nicole Avila navila
#I am using Python 3.7 
#  Part 1
# 1
def main ():
 print("Hello World")
 name = input( "What's your name?")
 print("Hello,", name)
 color = input("What's your favorite color?")
 stress = input("Are you stressed out? If so type stressed out")
if stress == "stressed out":
  print( "You like the color ", color, " and your are currently", stress, "You should consider therapy")
else:
  print("You like the color ", color, " and your are currently", stress, ".That's good!")

# 2: Convert Celsius to Farenheit
def celsius():
    celsius = eval(input("What is the temperature in celsius "))
    Farenheit = 9 / 5 * celsius + 32
   for x in range (5):
     print(Farenheit)

# 3 Unit Conversion
def convert():
  print("Hello! Welcome to Conversion! A simple app that converts minutes to hours! Simply    type in the amount of minutes and I'll tell you how many hours that is. ")

minutes = int(input("Minutes: "))
hours = int(input(minutes/60))
print ("Hours: ", hours)

# 4 Slope.. but really average  program to sum a series of numbers entered by the user
def slope():
  print ("Hello! This is a average conversion app. ")
  total = int(input("How many numbers do you want to average "))
  numbers = 0
if True:
  for x in range (total):

    number = int(input("Type next number: "))
    numbers+= number
        
  average = numbers/total
  print(average)
else: 
  print("type a real number ")

  # 5 fibonacci 
# make a position marker that will hold the person's position they are looking for 
position= int(input("Welcome! Which position are you looking for? "))
  if position == 1 or position == 2 :
    print (1)
    first = 1
    second = 2
  else: 
    first = 1
    second = 1
#given that the position equals 1 or 2 a for loop will run in the range offers and second 
  for i in range(position-2):
# a temporary value will hold the position of second 
    temp = second
    second = first + second 
    first =temp
  print (second)

# PART TWO!

# Figure out the amount of coins you can give out to the customer while ensure that it's the least number of coins possible. 
def coin_change(cents):
# This if statement will check to see whether the number owed is not negative. If it’s negative or equal to 0 it will print “error, cents must be positive” 
 
if cents <=0:
         print (error, cents must be positive”
else:
# If the number of cents is bigger than 0 than it will run the else statement.  quarter = cents// 25 basically means that it’ll ask whether the cents // 25  is a whole number. If it is then the program will run and give an output of quarters. For the rest I will just use a modulus and then divide the outcome by 10 to tell whether it is a whole number or not. 

     	quarter = cents // 25
     	dime = (cents % 25) // 10
	nickel = cents % 25 % 10 //5
	penny = cents % 5

	print “The number of coins for” , cents. “cents are:”
	print “quarters:”, quarter
	print “Dimes:”, dime
	print “nickels:”, nickel
	print “Pennies:", penny

