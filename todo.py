HELP = """
help - список команд
add - добавить событие
show - показать элемент
remove - удалить элемент
exit - закрыть программу
"""

todo = {}
userUnswer = 0

print("Ввудите команду")
print("Для вывода списака команд введите help")

while True:
  userUnswer = input()

  if userUnswer == "exit":
    print ("Программа закрыта")
    break
  elif userUnswer == "help":
    print(HELP)
  elif userUnswer == "add":
    print("Событие добавленно")
  elif userUnswer == "exit":
    print("Событие удалено")
  elif userUnswer == "show":
    print("Ку!")
  else:
    print("Введина некоректнная команда")
    print("Для вывода списака команд введите help")