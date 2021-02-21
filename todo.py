import time
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
    usrKey = input("Введите дату события в формате дд.мм.гггг\n")
     
    try:
      time.strptime(usrKey, '%d.%m.%Y')
    except ValueError:
      print('Не правильный формат даты')
      continue

    usrValue = input("Что нужно сделать?\n")

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


