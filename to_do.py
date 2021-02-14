HELP = """
help - список команд
add - добавить событие 
show - покозать  события 
remowe - удалить элемент
exit - закрыть программу 
"""

todo = {}
userUnswer = 0

print("Введите команду")
print("Для вывода списка команд введите help")

while True:
 userUnswer = input().lower()

if userUnswer == "exit":
  print("программа закрыта")
  break
elif userUnswer == "help":
  print(HELP) 
elif userUnswer == "add":
  print("Введите дату события в формате дд,мм,гггг")
  usrKey = input()

check = usrKey.split(".")
for i in check:
  print(i.sdigit())
  if i.sdigit():
    check = False
  else:
    check = True
    
if check:
  print("Не верный формат даты")
  continue

 print("Что нужно сделать?")
  usrValue = input()

  todo[ usrKey ] = usrValue
  print("событие добавлено") 
elif userUnswer == "remove":
  print("Событие удалено") 
elif userUnswer == "show":
  print("\n Увас запланировано:")
  
  for i in sorted( todo.keys() ):
    print(i + "\t" + todo.keys[i])
else:
  print("Не коректная команда") 
  print("Для выводы списка команд введите help") 