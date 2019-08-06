# PART TWO! 

# Figure out the amount of coins you can give out to the customer while ensure that it's the least number of coins possible. 
def coin_change(): 
# This if statement will check to see whether the number owed is not negative. If it’s negative or equal to 0 it will print error, cents must be positive  break
  cents = int(eval(input("Cents: ")))
  if cents <=0: 
      print ("error, cents must be positive")
  else: 
  # If the number of cents is bigger than 0 than it will run the else statement.  quarter = cents// 25 basically means that it’ll ask whether the cents // 25  is a whole number. If it is then the program will run and give an output of quarters. For the rest I will just use a modulus and then divide the outcome by 10 to tell whether it is a whole number or not.  

      quarter = cents // 25
      dime = (cents % 25) // 10
      nickel = cents % 25 % 10 // 5
      penny = cents % 5
  print ("The number of coins for " , cents, "cents are:") 
  print ("quarters:", quarter) 
  print ("Dimes:", dime)
  print ("nickels:", nickel) 
  print ("Pennies:", penny) 
coin_change()