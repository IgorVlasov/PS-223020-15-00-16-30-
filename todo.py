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
  userUnswer = input().lower()
  if userUnswer == "exit":
    print("программа закрыта")
    breake
  elif userUnswer == "help":
    print(HELP)
  elif userUnswer == "add":

    print("Введите дату события дд.мм.гггг")
    key = input()

    check = key.split(".")
    for i in check:
      if i.isdigit():
        check = false
      else:
        check = true
    if check:
      print("введите правильный формат даты")
      continue

  
    print("какое событие?")
    value = input()
    todo[key] = value

    print("событие добавлено")
  elif userUnswer == "remove":
    print("событие удалено")
  elif userUnswer == "show":
    print("\n У вас запланировано:")
    for i in sorted(todo.keys()):
      print(i + "\t" + todo[i])
  else:
    print("Не корректная команда")
    print("Для вывода команд введите help")