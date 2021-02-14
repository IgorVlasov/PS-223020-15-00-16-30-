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
  userUnswer = input()

  if userUnswer == "exit":
    print("Программа закрыта")
    break
  elif userUnswer == "help":
    print(HELP)
  elif userUnswer == "add":
    print("Событие добавлено")
  elif userUnswer == "remove":
    print("Событие удалено")
  elif userUnswer == "show":
    print("Ку!")
  else:
    print("Не корректная команда")
    print("для вывода списка команд введие help")


