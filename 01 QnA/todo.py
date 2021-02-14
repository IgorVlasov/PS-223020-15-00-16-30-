help = """
help - помощь
add - добавить
show - показать
remove - удальть эллемент
exit - выход
"""

todo = {}
userAns = 0
print("Enter command")
print ("for help enter'help'")

while True:
	userAns = input()
	if userAns == "exit":
		print("Programm has stop")
		break
	elif userAns == "help":
		print(help)
	elif userAns == "add":
		print("Event has add")
	elif userAns == "remove":
		print("Event has remove")
	elif userAns == "show":
		print("abc")
	else:
		print("I don't understand you...")
		print ("for help enter'help'")
