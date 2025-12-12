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


  <details>
    <summary>3. 🔑Password Manager</summary>

  ## 📌 Notes

This is a **console-based Password Manager** written in Python.
It saves account credentials (website, username, password) inside a **JSON file**, allowing the user to generate passwords, store them, preview them, and delete them safely.

---

## ⚙️ Features


 - 🔑 Generate random passwords

 - ➕ Save website + username + password

 - 📁 Stores all data inside a JSON file

 - 👀 Show all saved passwords

 - 🗑 Delete a specific website entry

 - 💾 Keeps data permanently even after closing the program

 - 🛡 Blocks deletion if the site doesn’t exist

 - ❗ Prevents showing or deleting empty data

   ---

  ## 🔍 Function Overview 
```create_random_password()```

 - Asks user for desired password length

 - Uses built-in printable characters (digits, symbols, letters)

 - Generates a secure random password

 - Displays it on screen (does not save automatically)

   ``create_file()``
 - Checks if passwords.json exists

 - If not, creates it

 - Initializes it as an empty JSON dictionary: {}

   ``load_passwords()``
 - Opens passwords.json and reads its contents

 - Returns all stored credentials as a Python dictionary

``save_passwords(data)``
 - Saves the updated dictionary back to passwords.json

 - Uses indent=4 for readable formatting

 - Overwrites the old file safely

``add_password()``

 - Asks the user for:

     - 🌐 Website

     - 👤 Username

     - 🔑 Password

 - Adds values to the JSON dictionary

 - Saves instantly

 - Confirms success

 ``show_password()``
  - Displays all saved credentials in a formatted table:

    ``🌐 Site | 👤 Username | 🔑 Password``


 - If no passwords are stored, shows a warning

``delete_password()``
 - Asks for a website name

 - Checks if it exists in the database

 - If found, confirms with user (Y/N)

 - Deletes only after approval

 - Cancels safely if declined

``menu()``
 - Displays program options in a loop:
  ```
    1. Create a new password
    2. Add a password
    3. Show all passwords
    4. Delete a password
    5. Exit
  ```


 - Calls the appropriate functions based on user choice

 - Ends the program when “Exit” is selected

 ---

 ## 💻 Mini Project to Practice Python Basics Such As:

 - 📦 JSON file handling

 - 🔁 Loops and control flow

 - 🧠 Logic & decision making

 - 🔤 String manipulation

 - 🎛 Console input/output

 - 📄 Working with dictionaries (dict)

 - 🎲 Random password generation
  
  </details>


  <details>
  <summary>3. 🃏 Blackjack Game (Python Console App)</summary>

  ---

  ## Notes:

  This is a **console-based Blackjack game** developed in **Python**, following object-oriented programming principles.
  The game simulates a realistic Blackjack experience with a player and a dealer, using multiple decks, automatic reshuffling, and standard Blackjack rules.

  ---

  ## ⚙️ Features:

   - 🃏 **Realistic Blackjack gameplay** (Player vs Dealer)

   - 🧩 **Object-Oriented Design** with separate classes for Card, Deck, Player, Dealer, and Game logic

   - 🔁 **Multiple decks support** (default: 6 decks)

   - 🔄 **Automatic deck reshuffle** when cards run low

   - 🎯 **Accurate score calculation**, including Ace value adjustment (1 or 11)

   - 🃎 **Natural Blackjack detection** (player or dealer)

   - 🤖 **Dealer logic** – dealer must hit until reaching 17

   - ⌨️ **Interactive user input** (Hit / Stand)

   - 🔁 **Replay option** after each round

  ---

  ## 🔍 Class & Method Overview

  ### **Card**
   - Represents a single playing card (rank and suit)
   - **get_value()** – returns the card’s Blackjack value
   - **__str__()** – returns a readable card representation

  ### **Deck**
   - Creates and manages one or more standard card decks
   - **shuffle()** – shuffles all cards randomly
   - **draw()** – draws a card and reshuffles automatically if the deck is low

  ### **Player**
   - Manages the player’s hand and score
   - **add_card()** – adds a card to the hand
   - **get_score()** – calculates total hand score with Ace handling
   - **show_hand()** – displays cards and score
   - **reset_hand()** – clears the hand for a new round

  ### **Dealer (inherits Player)**
   - Overrides **show_hand()** to hide one card until reveal
   - Reveals full hand during the dealer’s turn

  ### **BlackjackGame**
   - Controls the overall game flow
   - **deal_initial_cards()** – deals two cards to player and dealer
   - **check_for_natural_blackjack()** – checks for immediate Blackjack
   - **player_turn()** – handles player actions (Hit / Stand)
   - **dealer_turn()** – applies dealer rules (hit until 17)
   - **determine_winner()** – compares scores and declares the result
   - **play_round()** – runs a full game round

  ---

  ## 💻 Mini project to practice Python concepts such as:

   - Object-Oriented Programming (OOP)

   - Class inheritance and method overriding

   - Game logic and flow control

   - User input handling

   - Conditional logic and loops

   - Working with randomization

   - Clean code structure and readability

  ---
</details>
  
