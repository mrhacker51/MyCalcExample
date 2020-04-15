def function(num1,num2,user):
	if user not in "+-*/":
		return "Choose : +-*/"

	if user == "+":
		return str(num1) + " " + user + " " + str(num2) + " = " + str(num1+num2)
	elif user == "-":
		return str(num1) + " " + user + " " + str(num2) + " = " + str(num1-num2)
	elif user == "*":
		return str(num1) + " " + user + " " + str(num2) + " = " + str(num1*num2)
	elif user == "/":
		return str(num1) + " " + user + " " + str(num2) + " = " + str(num1/num2)

while True:
	num1 = int(input("Please enter number one  : "))
	num2 = int(input("Please enter number two  : "))
	user = input("Choose operation  : + - * / ")

	print(function(num1,num2,user))
