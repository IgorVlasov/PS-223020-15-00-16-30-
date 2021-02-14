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
  userUnswer = input().lower()

  if userUnswer == "exit":
    print ("Программа закрыта")
    break
  elif userUnswer == "help":
    print(HELP)
  elif userUnswer == "add":
    userKey = input()
    print("Введите дату события в формате дд.мм.гггг")
    check = userKey.split("."): 
    print(check)
    for i in check:
      if i.isdigit():
        check = False
      else:
        check = True
    if check:
      print("не верно формат даты")
      continue


        

    
    print("Что нужно сделать?")
    userValue = input()
    

    todo[userKey] = userValue
    print("Событие добавленно")
  elif userUnswer == "exit":
    print("Событие удалено")
  elif userUnswer == "show":
    print("\n У вас запланированно:")
    print(todo)
    for i in sorted( todo.keys() ):
      print(i + "\t" + todo[i])

  else:
    print("Введина некоректнная команда")
    print("Для вывода списака команд введите help")