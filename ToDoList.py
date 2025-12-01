# create new line for every item on list (DONE)
# TO ADD: In remove task, error if user input number out of range. 
# TO ADD: Undo function

myToDoList = ["clean dishes", "do math homework", "cook lunch"]
# quantTask = len(myToDoList)
# taskNum = (quantTask - selTask)

def myList():
    print("To be done!")
    for i, task in enumerate(myToDoList, start=1):
        format = f"{i}. {task}"
        print(format)

def addTask():
    myList()
    add = str(input("Task to be added: "))
    myToDoList.append(add)
    myList()
    
def delTask():
    myList()
    remove = int(input("Select task to be removed: "))
    taskNum = (remove - 1)
    del myToDoList[taskNum]
    myList()

def editTask():
    myList()
    selTask = int(input("Select Task to edit: "))
    taskNum = (selTask -1)
    myToDoList[taskNum] = input("Edit Task to: ")
    myList()

def selAction():
    action = str(input("What to do? \nA = Add Task \nB = Remove Task \nC = Edit Task \nD = Exit "))
    return action



while True:
    print("WELCOME TO YOUR TO-DO LIST!")

    select = selAction()

    if select == "A":
        addTask()
    elif select == "B":
        delTask()
    elif select == "C":
        editTask()
    elif select == "D":
        print("Done!")
        break
    else:
        print("INVALID ACTION")