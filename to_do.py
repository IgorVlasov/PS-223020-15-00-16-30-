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
 userUnswer = input()

if userUnswer =="exit":
  print("программа закрыта")
  break
elif userUnswer =="help":
  print(HELP) 
elif userUnswer =="add":
  print("событие добавлено") 
elif userUnswer =="remove":
  print("Событие удалено") 
elif userUnswer =="show":
  print("Ку!")
else:
  print("Не коректная команда") 
  print("Для выводы списка команд введите help") 