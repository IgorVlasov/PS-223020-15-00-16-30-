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

    print("Введите дату события")
    key = input()
    print("какое событие?")
    value = input()
    todo[key] = value

    print("событие добавлено")
  elif userUnswer == "remove":
    print("событие удалено")
  elif userUnswer == "show":
    print("\n У вас запланировано:")
    for i in todo.keys():
      print(todo[i])
  else:
    print("Не корректная команда")
    print("Для вывода команд введите help")