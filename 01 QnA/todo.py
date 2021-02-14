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
	userAns = input().lower()
	if userAns == "exit":
		print("Programm has stop")
		break
	elif userAns == "help":
		print(help)
	elif userAns == "add":
		print("Enter events date in formate dd.mm.yyyy:")
		usrKey = input()

		check = usrKey.split('.')
		for i in check:
			if i.isdigit():
				check = True
			else: 
				check = False
				

		if check:
			print("it is not date!")
			continue


		print("what may you do?")
		usrValue = input()

		todo [usrKey] = usrValue

	elif userAns == "remove":
		print("Event has remove")
	elif userAns == "show":
		print("\nIn your plans:")
		for i in sorted(todo.keys()):
			print(i + ':' + todo[i] + "\t")
			
		
	else:
		print("I don't understand you...")
		print ("for help enter'help'")
