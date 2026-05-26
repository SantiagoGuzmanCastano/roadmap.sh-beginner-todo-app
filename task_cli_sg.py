import json  # para leer y guardar las tareas en el archivo JSON
import sys  # para leer los argumentos que escribes en la terminal
import os  # para verificar si el archivo JSON existe
from datetime import datetime  # para guardar la fecha de creacion y actualizacion

TASK_FILE = "all_tasks.json"


def load_tasks() -> list[dict]:
    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r") as f:
        data = json.load(f)

        if not isinstance(data, list):
            return []
        return data


def save_tasks(task: list[dict]):
    with open(TASK_FILE, "w") as f:
        json.dump(task, f, indent=4)


def add_task(description: str):
    all_tasks = load_tasks()

    setId: int

    if not all_tasks:
        setId = 1
    else:
        highestTask = 0
        for task in all_tasks:
            if task["ID"] > highestTask:
                highestTask = task["ID"]
        setId = highestTask +1
    task = {
        "ID": setId,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat(),
    }
    all_tasks.append(task)
    save_tasks(all_tasks)


def delete_task(id: int):
    all_tasks = load_tasks()
    for i in all_tasks:
        if i["ID"] == id:
            print(f"Task {i['description']} (ID: {i['ID']}), has been deleted.")
            all_tasks.remove(i)
            save_tasks(all_tasks)
            return
    print("Task not found")


def delete_all_task():
    all_tasks = load_tasks()
    all_tasks = []
    save_tasks(all_tasks)
    return


def list_tasks(status=None):
    all_tasks = load_tasks()

    if not all_tasks:
        print("There are no tasks")
        return
    

    if status is not None:
        all_tasks = [task for task in all_tasks if task['status'] == status]
        if not all_tasks:
            print(f"No tasks with status '{status}' found")
            return

    for i in all_tasks:
        created = datetime.fromisoformat(i["createdAt"])
        updated = datetime.fromisoformat(i["updatedAt"])
        print(f"ID: {i['ID']} | Task: {i['description']} | Status: {i['status']}")
        print(
            f"Created At: {created.strftime('%d/%m/%Y %H:%M')} | Last Update At: {updated.strftime('%d/%m/%Y %H:%M')}"
        )
        print("")

# actualiza nombre
def update_task(id: int, description: str):
    all_tasks = load_tasks()
    for i in all_tasks:
        if i["ID"] == id:
            if description:
                i["description"] = description
                i["updatedAt"] = datetime.now().isoformat()
                print(f"Task {i['ID']} has been updated")
                save_tasks(all_tasks)

                return
            print("Cannot update the task without giving the new task name")

    print(f"Task ID:{id} not found")


def change_status(id: int, statusResponse: str):
    all_tasks = load_tasks()

    newStatus = ''

    if statusResponse == 'mark-to-do':
        newStatus= 'todo'
    elif statusResponse == 'mark-in-progress':
        newStatus= 'in-progress'
    elif statusResponse == 'mark-done':
        newStatus= 'done'
    else:
        print('Status not valid')
        return    
    
    task_found = False

    for task in all_tasks:
        if task["ID"] == id:
            task_found = True
            if task["status"] == newStatus:
                print("The task is already that status")
            else:
                task["status"] = newStatus
                save_tasks(all_tasks)
                print("Task status changed")
        
    if not task_found:
        print(f'Task ID:{id} not found')
        return






def main():
    args = sys.argv[1:]
    # ["add", "Comprar leche"]
    # ["delete", "1"]

    if not args:
        print("Invalid response. Try again")

    command = args[0].lower()

    if command == "add":
        if len(args) < 2:
            print("You cant create a task without name. Please enter task name")
            return
        add_task(args[1])

    elif command == "delete":
        if len(args) < 2:
            print(
                "You cant delete a task without giving its id. Please enter task ID to delete"
            )
            return
        else:
            delete_task(int(args[1]))

    elif command == "clear":
        delete_all_task()

    elif command == "list":
        if len(args) == 1:
            list_tasks(status = None)
        elif len(args) == 2:
            list_tasks(status = args[1])

    elif command == "update":
        if len(args) < 2:
            print("Please enter task id and name.")
            return
        elif len(args) < 3:
            print("Please enter task name.")
            return
        else:
            update_task(int(args[1]), args[2])

    elif command in ["mark-to-do", "mark-in-progress", "mark-done"]:
        if len(args) < 2:
            print("Please enter task id.")
            return
        change_status(statusResponse=args[0], id=int(args[1]))
    else:
        print("Status not valid")


if __name__ == "__main__":
    main()
