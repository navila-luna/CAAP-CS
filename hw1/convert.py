# 3 Unit Conversion 
def convert():
	print("Hello! Welcome to Conversion! A simple app that converts minutes to hours! "
		+"Simply type in the amount of minutes and I'll tell you how many hours that is.")
	minutes = eval(input("Minutes: "))
	hours = minutes/60
	print ("Hours: ", hours) 
convert()