HELP = """
help    - список команд
add     - добавть событие
show    - показать события
remove  - удалить элемент
exit    - закрыть программу
"""

todo = {}
userUnswer = 0

print("Введите команду")
print("для вывода списка команд введие help")

while True:
  userUnswer = input().lower()

  if userUnswer == "exit":
    print("Программа закрыта")
    break
  elif userUnswer == "help":
    print(HELP)
  elif userUnswer == "add":
    print("Введите дату события в формате дд.мм.гггг")
    usrKey = input()
    
    check = False
    for i in usrKey.split("."):
      if i.isdigit():
        check = False
      else:
        check = True
        
    if check:
      print("не верный формат даты")
      continue

    print("Что нужно сделать?")
    usrValue = input()

    todo[ usrKey ] = usrValue
    print("Событие добавлено")
  elif userUnswer == "remove":
    print("Событие удалено")
  elif userUnswer == "show":
    print("\nУ вас запланировано:")
    print(todo)
    for i in sorted( todo.keys() ):
      print(i + "\t" + todo[i])
  else:
    print("Не корректная команда")
    print("для вывода списка команд введие help")


