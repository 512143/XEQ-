HELP = """
add - добавить задачу
show - показатб задачу
done - убрать выполн задачу
exit - закрыть прилож
"""

todo ={}
print ("введите комаду или help")

while True:
  userAnswer = input()

  if userAnswer == "add":
    userDate = input("VVedi daty:\n")
    userTask = input("Chto nujno sdelatb?")
    todo[ userDate] = userTask
    print(f"[ {userDate} ] - AddTask'{userTask}'")
    
    if userDate in todo.keys():
      todo[userDate].append(userTask)
    else:
      todo[userDate]=[userTask]
    print(f"[{userDate}]-добавлена задача'{userTask}'")

  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "show":
    for date in todo.keys():
      print( f"[{date}] - \t {todo[date] }")
    print("Rabotaet")
  elif userAnswer == "exit":
    break
  elif userAnswer == "done":
    print("Rabotaet")
