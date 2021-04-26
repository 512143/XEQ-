import time



HELP = """
add - добавить задачу
show - показатб задачу
done - убрать выполн задачу
exit - закрыть прилож
"""

todo ={}

def checkDate(date):
  try:
    time.strptime(date,"%d.%m.%Y")
    return True
  except ValueError:
    print("Error.Неправильная дата")
    return False

def add(command,userAnswer):
  if command == 1:
    #получить дату
  elif command == 2:
    #получить task и добавить в todo
  userDate = input("VVedi daty:\n")
  if checkDate(userDate)==False:
        continue
      userTask = input("Chto nujno sdelatb?")

      if userDate in todo.keys():
        todo[userDate].append(userTask)
     else:
       todo[userDate]=[userTask]
      print(f"[{userDate}]-добавлена задача'{userTask}'") 

print ("введите комаду или help")

while True:
  userAnswer = input()

  if userAnswer == "add":
    

  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "show":
    for date in sorted(todo.keys()):
      for date in todo.keys():
        for tasks in todo[ date]:
          print( f"[{date}] -  {tasks}")
    print("Rabotaet")
  elif userAnswer == "exit":
    break
  elif userAnswer == "done":
    print("Rabotaet")
