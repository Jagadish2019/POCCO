#  Ask the user to enter a number, If it is under 10, 
# display the message "Too low", if their number is between 10 and 20 Correct
# other display too high

num = int(input("Enter a number of your choice: "))

if num < 10:
	print("The number you have entered is Too Low")
else:
	if num >=10 and num <=20:
		print("Correct")
	else:
		print("The number is too high")

print("*********** Thanks a lot **********")