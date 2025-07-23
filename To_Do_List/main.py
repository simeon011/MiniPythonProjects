import os


def create_file():
    file_name = input('Enter file name: ').strip()

    if '.' not in file_name:
        file_name += ".txt"
    else:
        check_type = file_name.split('.')
        if check_type[1] != 'txt':
            print('⚠️ You can only create .txt files')
            return

    if os.path.exists(file_name):
        raise FileExistsError(f'❌ File {file_name} already exists')
    else:
        with open(file_name, 'w') as f:
            print(f'✅ Creating {file_name}')
            f.write('Tasks:\n')


def show_tasks():
    file_name = input('Enter file name: ').strip()
    if '.' not in file_name:
        file_name += ".txt"

    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            print(f.read())
    else:
        print('❌No such file exists.')
        return


def add_tasks():
    new_tasks = []
    file_name = input('Enter file name: ').strip()
    if '.' not in file_name:
        file_name += ".txt"

    if not os.path.exists(file_name):
        print('❌ No such file exists.')
        return

    with open(file_name, 'r') as f:
        existing_tasks = [line.strip() for line in f.readlines()]

    task_number = len(existing_tasks)

    while True:
        new_task = input('Enter new task (or "end" to finish): ').strip()
        if new_task.lower() == "end":
            break

        stripped_existing = [line[line.find(' ') + 1:] if '.' in line else line for line in existing_tasks]

        if new_task in stripped_existing:
            print('⚠️ This task already exists.')
        else:
            task_line = f"{task_number}. {new_task}"
            new_tasks.append(task_line)
            existing_tasks.append(task_line)
            task_number += 1
            print(f'✅ You added: {task_line}')

    with open(file_name, 'a') as f:
        for task in new_tasks:
            f.write(task + '\n')

    print(f'📝 {len(new_tasks)} tasks added to {file_name}')


def delete_tasks():
    file_name = input('Enter file name: ').strip()
    if '.' not in file_name:
        file_name += ".txt"

    if not os.path.exists(file_name):
        print('❌ No such file exists.')
        return

    with open(file_name, 'r') as f:
        print(f.read())

    with open(file_name, 'r') as f:
        existing_tasks = [line.strip() for line in f.readlines()]

    number = input('\n🗑️ Which task number do you want to delete? (e.g. 1): ').strip()
    task_found = False
    for task in existing_tasks:
        if task.startswith(f"{number}. "):
            existing_tasks.remove(task)
            task_found = True
            break

    if task_found:
        with open(file_name, 'w') as f:
            for task in existing_tasks:
                f.write(task + '\n')
        print(f'✅ Task {number} has been deleted.')
    else:
        print('⚠️ Task not found.')


def save_and_leave():
    print("👋Goodbye")


print('1. Create a file')  #--
print('2. Show all tasks')  #--
print('3. Add a task')
print('4. Delete a task')
print('5. Save a task and leave')

while True:
    choose = input("Choose a option: ")
    if choose == '1':
        create_file()
    elif choose == '2':
        show_tasks()
    elif choose == '3':
        add_tasks()
    elif choose == '4':
        delete_tasks()
    elif choose == '5':
        save_and_leave()
        break
    else:
        print('❗ Invalid option. Please choose from 1 to 5.')