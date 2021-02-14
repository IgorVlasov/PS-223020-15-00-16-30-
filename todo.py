HELP = """"
help - списко команд
add - добавить событие
show - показать
remove - удалить
exit - закрыть прогармму
"""

todo = {}
userUnswer = 0

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
    print("Событие добавлено")
  elif userUnswer == "remove":
    print("Событие удалено")
  elif userUnswer == "show":
    print("Ку!")
  else:
    print("Не корректная команда")
    print("Для вывода списка команд введите help ")
