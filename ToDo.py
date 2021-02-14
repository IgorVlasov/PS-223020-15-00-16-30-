HELP ="""
help - список команд
add - добавить событие
show - показать событие
remove - удалить элемент
exit - закрыть программу
"""

ToDo = {}
userUnswer = {}

print("Введите команду")
print("для вывода сптска команд введите help")

while True:
  userUnswer = input().lower()

  if userUnswer == "exit":
    print ("Программа закрыта")
    break
  elif userUnswer == "help":
    print (HELP)

  elif userUnswer == "add":
    print("Введите дату события в формате дд.мм.гггг")
    
    userKey = input()

    check = userKey.split(".")
    for i in check:
      if i.isdigit():
        continue
      else:
        check = True
        break
    if check:
      continue

    print("Что нужно сделать?")
    userValue = input()
    
    ToDo[userKey] = userValue
    print ("Событие добавлено")
  elif userUnswer == "exit":
    print ("Событие удалено")
  elif userUnswer == "show":
    print("\n у вас запланированно:")
    print(ToDo)
    for i in ToDo.keys().sorted():
      print(i + "\t" + ToDo[i])
  else:
    print ("Не корректная команда")
    print ("для вывода списка команд введите help")
   


