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
    uDate = input("Введите дату события в формате дд.мм.гггг\n")
     
    try:
      time.strptime(uDate, '%d.%m.%Y')
    except ValueError:
      print('Не правильный формат даты')
      continue

    uTask = input("Что нужно сделать?\n")

    if uDate in todo:
      todo[ uDate].append( uTask )
    else:
      todo[ uDate ] = [uTask]
   
    print(f"На {uDate} нужно выполнить '{uTask}'.")

  elif userUnswer == "remove":
    print("Событие удалено")
  elif userUnswer == "show":
    print("\nУ вас запланировано:")

    for i in sorted( todo.keys() ):
      print(i + "\t" + todo[i])
  else:
    print("Не корректная команда")
    print("для вывода списка команд введие help")
