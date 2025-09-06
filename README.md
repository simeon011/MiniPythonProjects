# MiniPythonProjects

Here you can see mini projects I have created in my free time. 

Enjoy🤗

## Table of Contents:
<details>
<summary>1. 📝 To-Do List</summary>
  
  ### Notes:
  
  This is a console-based to-do list application written in Python. It allows users to create .txt files as task lists, add tasks with automatic numbering, view tasks, delete specific tasks by number, and exit safely.
  ## ⚙️ Features:
  
  - ✅ Create a new task file (only .txt allowed)
  - 📄 Show all tasks in a file
  - ➕ Add tasks (prevents duplicates, auto-numbered)
  - 🗑️ Delete a task by its number
  - 💾 Exit the program gracefully
  ## 🔍 Function Overview
  
  - create_file()
  
    - Prompts the user for a file name
    - Automatically appends .txt if no extension
    - Refuses to create non-txt files
    - Prevents overwriting existing files
  - show_tasks()
  
    - Opens and displays the contents of the selected file
  - add_tasks()
  
    - Opens existing file
    - Asks the user to input new tasks one by one
    - Prevents duplicates
    - Appends tasks with auto-incremented numbers
- delete_tasks()

  - Displays the current task list
  - Prompts the user to enter the task number to delete
  - Removes the task and rewrites the file
- save_and_leave()

  - Exits the program
 ## 💻Mini project to practice Python basics such as: 
 
 - File handling
- Loops
- Conditional logic
- List operations
- String manipulation
- Console input/output
## 📷Preview
<img width="271" height="197" alt="Screenshot 2025-07-23 233020" src="https://github.com/user-attachments/assets/04f54651-57c6-4466-9610-e2138b24e14e" />
</details>


<details>
  <summary>2. ✅ To-Do App (Tkinter)</summary>

  ---

  ## Notes:

  This is a **desktop to-do list application** written in**Python with Tkinter**.
  It allows users to create a titled to-do list, add tasks dynamically, and mark them as In Progress or Completed with an interactive interface.
  
  ---

  ## ⚙️ Features:

   - 📝 **Create a new to-do list** with a custom title

   - ➕ **Add tasks** dynamically with an input field

   - 🔄 **Toggle task status** between In Progress and Completed

   - ✅ Completed tasks are shown with a **strike-through effect**

   - ⚠️ Validation – prevents adding empty tasks

   - 🎨 Simple and user-friendly GUI
  
  ---

  ## 🔍 Function Overview

   - **create_title()**

      - Prompts the user to enter a title for the to-do list

      - Updates the window title dynamically

      - Shows the "Add" button after the title is set

  - **show_add_button()**

      - Displays the "Add" button to insert a new task

   - **add_task_row()**

      - Provides an entry field to add a task

      - Prevents saving empty tasks

      - Creates a row with the task text and a status checkbox

      - Marks tasks with strike-through when completed

  - **toggle_status()**

      - Switches a task between In Progress and Completed

      - Updates task label style accordingly

  - **init_tasks_frame()**

      - Initializes the frame that holds all task rows
  
  ---

  ## 💻 Mini project to practice Python basics such as:

   - Tkinter GUI programming

   - Event handling with buttons and checkboxes

   - Dynamic widget creation and management

   - Conditional logic

   - String validation

   - List management for tasks
  
  ---

  ## 📷 Preview
  <img width="498" height="452" alt="image" src="https://github.com/user-attachments/assets/9a126f57-af1f-41f3-b141-3e0203fb9fd5" />
  <img width="495" height="443" alt="image" src="https://github.com/user-attachments/assets/b48e102f-8b33-4e6a-8171-04d9ed2c00a8" />



</details>

