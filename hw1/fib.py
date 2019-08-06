 # 5 fibonacci 
# make a position marker that will hold the person's position they are looking for 
def fib():
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
  print(second) 
fib()