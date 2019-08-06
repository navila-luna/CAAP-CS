def hello(): 
 	print("Hello World") 
 	name = input( "What's your name?") 
 	print("Hello,", name) 
 	color = input("What's your favorite color?") 
 	stress = input("Are you stressed out? If so type stressed out") 
 	if stress == "stressed out": 
 		print( "You like the color ", color, " and your are currently", stress, "You should consider therapy") 
 	else: 
 		print("You like the color ", color, " and your are currently", stress, ".That's good!")

hello()