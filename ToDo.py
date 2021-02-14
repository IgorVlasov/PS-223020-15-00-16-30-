HELP="""
help- список команд
add-добавить событие 
show-показать события
remove-удалить элемент
stop-закрыть программу
"""




todo={}
userAnswer=0

print("Введите команду")
print("Для вывода списка команд введите help")

while True:
  userAnswer=input()

  if userAnswer=="stop":
    print("Программа закрыта")
    break
  elif userAnswer =="help":
    print("Help")
  elif userAnswer =="add":
    print("Введите дату события")
    print("В формате:dd.mm.yyyy")
    userKey=input()

    check=False
    check=userKey.split(".")

    for i in check:
      if i.isdigit():
        check=False
      else:
        check = True
        break

  if check:
    print("Не верный формат даты")
    continue
   

    print("Что нужно сделать?")
    userValue=input()

    todo[userKey]=userValue

    print("Событие добавлено")
  elif userAnswer =="show":
    print("\nУ вас запланировано:")
    print(todo)
    for i in sorted(todo.keys()):
      print(i+"\t"+todo[i])

    print("Ку")
  elif userAnswer =="remove":
    print("Событие удалено")
  else:
    print("Не корректная команда")
    print("Для вывода списка команд введите help") 