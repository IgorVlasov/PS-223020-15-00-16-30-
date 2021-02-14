HELP = """"
help - списко команд
add - добавить событие
show - показать
remove - удалить
exit - закрыть прогармму
"""

todo = {}
userUnswer = input().lower()

print("Введите команду")
print("Для вывода списка команд введите help")

while True:
  userUnswer = input()

  if userUnswer == "exit":
    print("Программа закрыта")
    break
  elif userUnswer == "help":
    print(HELP)
  elif userUnswer == "add":
    print("Введите дату события в формате дд.мм.гггг")
    usrKey = input()

  for i in usrKey.split(".")
  for i in check:
    if i.isdigit():
      check = False
    else:
      check = True
    

  if check:
    print("не верный формат даты")
    continue

    print("Что нужно делать?")
    usrValue = input()

    todo[ usrKey ] = usrValue
    print("Событие добавлено")
  elif userUnswer == "remove":
    print("Событие удалено")
  elif userUnswer == "show":
    print("\nУ вас запланировано:")
    for i in sorted(todo.keys()):
      print("\t" + todo[i])
  else:
    print("Не корректная команда")
    print("Для вывода списка команд введите help ")
