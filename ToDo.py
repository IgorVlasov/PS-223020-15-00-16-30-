HELP ="""
help - список команд
add - добавить событие
show - показать событие
remove - удалить элемент
exit - закрыть программу
"""

ToDo = {}
userUnswer = {}

print("Введите команду")
print("для вывода сптска команд введите help")

while True:
  userUnswer = input()

  if userUnswer == "exit":
    print ("Программа закрыта")
    break
  elif userUnswer == "help":
    print (HELP)

  elif userUnswer == "add":
    print ("Событие добавлено")
      
  elif userUnswer == "remove":
    print ("Событие удалено")
  
  
  elif userUnswer == "show":
    print ("Ку!")
  else:
    print ("Не корректная команда")
    print ("для вывода списка команд введите help")
   


