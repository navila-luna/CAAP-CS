# imports random madule form library
from random import randint

# the base class for the scenes. 
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene(). 
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

  def enter(self):
    print("Welcome to the matrix! You are stuck in a game where you are unkowingly trapped in a virtual reality. To escape you must complete a list of tasks that will challenge your strength, courage, artificial intelligence and digital technology has been used to make virtual realir")
    # print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
    #print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
    exit(1)

class RiddleTown(Scene):
  
  name = "RiddleTown"
   
   
  def enter(self):
    print (" Welcome to RiddleTown. A place where magicians, dwarves, and scholars seekings riddles to broaden their minds. The town a nice place, but in order to leave you must answer.If you get the riddle wrong you die. You want to leave because of a friend. The seeker gives you the following riddle: ")
    return self.action()
    
    
  def action(self):
    # this is the harder level that adds another riddle 
    harder = input("To make the level harder type 2.0")
    if harder == "2.0":
      response = input(" What word in the English language does the following: the first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great woman. What is the word?" )
      if response.lower() ==  "heroine":
        print("Correct! Now if you answer this next question correctly, you may pass to the next level!")
        response2 =  input(" I’m tall when I’m young, and I’m short when I’m old, what am I? ...I'm a ")
        if response2.lower() == "candle":
          print("Correct! You may now move on to the next level. You are one step closer to leaving the Matrix.")
          return self.exit_scene('highschool')
        else: 
          print("Welp. that was wrong. Guess you'll be staying in the matrix longer")
          return self.exit_scene('death')
      else: 
        print("Incorrect")
        return self.exit_scene('death')
# this is easier and will make you move on if u pass
    if harder != "2.0":
      response= input(" What word in the English language does the following: the first two letters signify a male, the first three letters signify a female, the first four letters signify a great, while the entire world signifies a great woman. What is the word?" )
      if response.lower() == "heroine":
          print("Correct! You may pass to the next level!")
          return self.exit_scene('highschool')
          # I want to create a return statement that will move the user to the next level without removing one of his three lives
      elif response == ":q":
          return self.exit_scene(response)
      else:
          print("Welp.That's the wrong answer.")
          # I want to create a return statement that will move the user to the beginning of THIS level while removing one of his three lives
          return self.exit_scene('death')
      
  def exit_scene(self, outcome):
    return outcome

class Highschool(Scene):
  
  name = 'highschool'
    

  def enter(self):
    print ("There are two path ways. One way will lead you out of level two and the other will kill you. ")
    return self.action()          
    

  def action(self):
    harder = input("To make the game harder type 2.0")
    count = 0
    #print("In this maze you are trapped in a shady black market organ institute. They are keeping you in to later remove your organs. You were originally locked in a room, but you managed to get out by punching the guard when he was handing you the lunch of the day. Now that you are out of your cell you run straight until you reach a point that has door to the left and another on the right.")
    #pathway = input("Which one do you open?")
    if harder == "2.0":
      print("In this maze you are trapped in a shady black market organ institute. They are keeping you in to later remove your organs. You were originally locked in a room, but you managed to get out by punching the guard when he was handing you the lunch of the day. Now that you are out of your cell you run straight until you reach a point that has door to the left and another on the right.")
      pathway = input("Which one do you open?")
      print("Welcome to the advanced level! Here, you'll be asked a Riddle by the end of the level.")
      if pathway.lower() == "left":
        print("You opened the left door to find a team of shady doctors performing surgery. One many sees you and before you know it. You wake up and to find yourself on a surgical table. You realized you made the wrong choice.")
        return self.exit_scene('death')
      elif pathway.lower() == "right":
        print("You opened the right door to find yourself back in high school. You see the students rushing down the hallway to get to their next class. In the corner of your eye you could see a big bully asking a shorter kid for his lunch money. As you keep walking through the hallway you can see through the class door windows students falling asleep. You begin to question whether this is all humane. After a couple of minutes of taking it all in, a girl asks why you are not in math class already. You head in with her to math class. Just as you do, the teacher hands out a math test. It's your calculus final. The teacher says that those who don't pass with a 100% will not be able to graduate. The rumor is though,those who don't graduate go missing...and end up in a shady place.")
      ques1 = (input("First question is what's the derivative of 4x^2? "))
      if ques1 == '8x':
        print("Correct!")
        count += 1
      ques2 = input("Second question is what's the integral of 16x^3? ") 
      if ques2 == '4x^4':
        print ("Correct!")
        count += 1
      else:
        print("Incorrect. ")
      ques3 = input("Third question: What is the derivative of 6+6x^4/4x? ")
      if ques3 == '24x^3':
        print("Correct!")
        count += 1
      ques4 =  input("4th question: What is the derivative of 5x^2 *x? ")    
      if ques4 == '10x + 5x^2':
        print( "Correct!")
        count += 5
      if count >= 3:
        print ("Congrats you won!")
        return self.exit_scene('fakefriends')
      else:
        print("Welp.You Lost...You will end up in that shady place... make sure to punch some guards..")
        return self.exit_scene('death')
    #CHECK !!
    # This makes the math questions harder in the sense that u need more write to win
    if  harder != "2.0":
      print("Welcome! In this maze you are trapped in a shady black market organ institute. They are keeping you in to later remove your organs. You were originally locked in a room, but you managed to get out by punching the guard when he was handing you the lunch of the day. Now that you are out of your cell you run straight until you reach a point that has door to the left and another on the right.")
      pathway = input("Which one do you open?")
      if pathway.lower() == "left":
         print("You opened the left door to find a team of shady doctors performing surgery. One many sees you and before you know it. You wake up and to find yourself on a surgical table. You realized you made the wrong choice.")
         return self.exit_scene('death')
      elif pathway == "right" or "Right":
        print("You opened the right door to find yourself back in high school. You see the students rushing down the hallway to get to their next class. In the corner of your eye you could see a big bully asking a shorter kid for his lunch money. As you keep walking through the hallway you can see through the class door windows students falling asleep. You begin to question whether this is all humane. After a couple of minutes of taking it all in, a girl asks why you are not in math class already. You head in with her to math class. Just as you do, the teacher hands out a math test. It's your calculus final. The teacher says that those who don't pass with a 100% will not be able to graduate. The rumor is though,those who don't graduate go missing...and end up in a shady place.")
        ques1 = (input("First question is what's the derivative of 4x^2? "))
        count = 0
        if ques1 == "8x":
          print("Correct!")
          count += 1
        ques2 = input("Second question is what's the integral of 16x^3? ") 
        if  ques2 == '4x^4':
          print ("Correct!")
          count += 1
        ques3 = input("Third question: What is the derivative of 6+6x^4/4x")
        if ques3 == "24x^3":
          print("Correct!")
          count += 1
        ques4 =  input("4th question: What is the derivative of 5x^2 *x")    
        if ques4 == "10x + 5x^2":
          print( "Correct!")
          count += 1
    if  count >= 2:
      print ("Congrats you won!")
      return self.exit_scene('fakefriends')
    else:
      print("Welp. You Lost... You will end up in that shady place... make sure to punch some guards..")
      return self.exit_scene('death')   

  def exit_scene(self, outcome):
    return outcome

class Fakefriends(Scene):
  name ='fakefriends'
            

  def enter(self):
    print("Welcome! You have reached level 3. Please, sit down. On the table in front of you are two cups. One has blue cool-aid linked with poison and the other one has regular blue cool aid... in a few minutes your friend Luna will be coming. You drink one cup and she drinks the other one. You choose your and her fate.")
    return self.action()
  def action(self):
    # If you choose the left then you die and if you choose right then you enter a high school and answer math questions
    choice = input("Which one shall it be? The one on the left or the one on the right?") 
    harder = input("To make the level harder, type 2.0")  
    if choice == "left":
      print("you died")
      return self.exit_scene('death') 

    elif choice == "right":
      print("Correct!")
      response = input(" I am an odd number. Take away a letter and I become even. What number am I? (write in words)")
      if response.lower() == "seven":
        print("Correct!")
        return self.exit_scene('rockpaperscissors')
      else:
        print("oof. That's wrong.") 
        return self.exit_scene('death')
    if harder == "2.0":
      resp = input("Okay Mr.Smarty Pants answer this riddle: What has four eyes but can’t see?")
      if resp.lower() == "mississippi":
        print("Congrats! You passed! You can move on now")
        return self.exit_scene('rockpaperscissors')
      else:
        print ("Welp. You died again.")
        return self.exit_scene('death')
    else:
      print("ERROR type left or right")

    if harder != "2.0":
      choice = input("Which one shall it be? The one on the left or the one on the right?")   
      if choice == "left":
        print("you died")
        return self.exit_scene('death')
                        
      elif choice == "right":
        print("Correct!")
        return self.exit_scene('rockpaperscissors')                   
      else:
        print("ERROR type left or right")
      # hopefully, this will change whether the drink will be with poison or not... 

  def exit_scene(self, outcome):
    return outcome

class Rockpaperscissors(Scene):
  name = 'rockpaperscissors'
  # play a game of rock paper and scissors you must win to move on and win overall... series of if stastements and a list to pick a move

  def enter(self):
      print("Welcome to level 4. Here is the rock paper scissor tournament. In this place the player is challenged to a game of rock paper scissors. You must win the match to move on to level 5. If you lose or tie, the people will decide who liked whose performance better. In the game, there are only three options: rock, paper, and scissors. When typing your result put it all in lowercase.")
      return self.action()
  def action(self):
    # create list
    t = ["rock", "paper", "scissors"]
    #create a random plat to the computer
    comp = t[randint(0,2)]
    #set player to False
    player = 0
    computer = 0
    while player == False:
    #set player to True
      player = input("Now on the count, 1 2 3 Rock Papers Scissors Shoot!\n Write Your Answer Lowercase: Rock Paper or Scissors\n >")
    if player == computer:
      print("It's a tie!")
    # people decide to let him move on
      return self.exit_scene('finished')
    cs player == "rock":
        if comp == "paper":
           print("Oof you lost. computer got ", comp, " cover you so you lose.")
           return self.exit_scene('death')
        if comp == "rock":
          print("It's a tie!")
          return self.exit_scene('death')
        else:
           print("you win ", player, " smashes ", comp)
           return self.exit_scene('finished')
    elif player == "paper":
        if comp == "scissors":
           print("You lose", computer, " cuts ", player)
           return self.exit_scene('death')
        if comp == "paper":
          print("It's a tie!")
          return self.exit_scene('death')
        else:
           print("You win!",player," covers", comp)
           return self.exit_scene('finished')
    elif player == "scissors":
        if comp == "rock":
           print("You lose...", comp," smashes", player)
           return self.exit_scene('death')
        if comp == "scissors":
          print("It's a tie!")
          return self.exit_scene('death')
        else:
            print("You win!", player, " cut", computer) 
            return self.exit_scene('finished')     
    else:
        print("Please check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]

    
  def exit_scene(self, outcome):
        return outcome      

                        
                        
                        
                        
                        
                        
                        