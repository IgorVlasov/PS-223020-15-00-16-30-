HELP = """
help   - список команд
add    - добавить  событие
show   - показать события
remove - удалить элемент
exit   - выход
"""
todo = {}
userUnswer = 0
print("введите команду")
print("для вывода списка команд введите help")

while True:
  userUnswer = input()
  if userUnswer == "exit":
    print("программа закрыта")
    breake
  elif userUnswer == "help":
    print(HELP)
  elif userUnswer == "add":
    print("событие добавлено")
  elif userUnswer == "remove":
    print("событие удалено")
  elif userUnswer == "show":
    print("Ky")
  else:
    print("Не корректная команда")
    print("Для вывода команд введите help")