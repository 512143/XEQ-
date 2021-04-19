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
    print("Работает")
  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "show":
    print("Rabotaet")
  elif userAnswer == "exit":
    break
  elif userAnswer == "done":
    print("Rabotaet")
