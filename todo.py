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
    print("Введите дату события")

    userKey = input()
    print("Что нужно сделать?")
    userValue = input()

    todo[userKey] = userValue
    print("Событие добавленно")
  elif userUnswer == "exit":
    print("Событие удалено")
  elif userUnswer == "show":
    print("\n У вас запланированно:")
    for i in todo.keys():
      print("\t" + todo[i])
    print("Ку!")
  else:
    print("Введина некоректнная команда")
    print("Для вывода списака команд введите help")