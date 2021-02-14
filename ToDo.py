HELP=""
help- список команд
add-добавить событие 
show-показать события
remove-удалить элемент
exit-закрыть программу

todo={}
userAnswer=0

print("Введите команду")
print("Для вывода списка команд введите help")

while True:
  userAnswer=input()

  if userAnswer=="exit":
    print("Программа закрыта")
    break
  elif userAnswer =="help":
    print("Help")
  elif userAnswer =="add":
    print("Событие добавлено")
  elif userAnswer =="show":
    print("Ку")
  elif userAnswer =="remove":
    print("Событие удалено")
   else:
     print("Не корректная команда")
     print("Для вывода списка команд введите help") 