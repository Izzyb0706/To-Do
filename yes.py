import json


def load_file():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("file not found")
    except json.JSONDecodeError:
        print("Invalid JSON")


def write_file(data):
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)


def view_status(status, data):
    for task in data:
        if task["status"] == status:
            print(f"Number:{task['number']} Task:{task["task"]}")


def action1(data):
    status = "complete"
    view_status(status, data)


def action2(data):
    status = "incomplete"
    view_status(status, data)


def action3(data):
    for task in data:
        print(f"Number:{task['number']} Task:{
              task["task"]} Status:{task['status']}")


def action4(data):
    number = input("What number task would you like to change ? : ")
    for task in data:
        if task['number'] == number:
            task['status'] = "complete"
            print("task marked as complete")
            return


def action5(data):
    number = len(data)+1
    task_name = input("Enter a name: ")
    data.append({"task": task_name, "number": number,
                "status": "incomplete"})
    data.sort(key=lambda x: x['number'])
    write_file(data)
    print("Task Added")


def main():
    while True:
        data = load_file()
        menu = input("""Please choose an option: 
    
    1. View completed tasks 
    
    2. View incomplete tasks 
    
    3. View all tasks                                                                     
    
    4. Mark a task as complete 
    
    5. Add a new task 
    
    6. Exit """)
        try:
            menu = int(menu)
            if menu == 1:
                action1(data)
            if menu == 2:
                action2(data)
            if menu == 3:
                action3(data)
            if menu == 4:
                action4(data)
            if menu == 5:
                action5(data)
            if menu == 6:
                quit()
        except ValueError:
            print("invalid choice")
            main()


if __name__ == "__main__":
    main()
