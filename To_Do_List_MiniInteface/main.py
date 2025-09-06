import tkinter as tk
from tkinter import messagebox

tasks_frame = None
add_btn = None
task_rows = []
editor_widgets = []


def create_title():
    start_btn.destroy()

    label = tk.Label(root, text='Enter a title')
    label.place(relx=0.5, rely=0.4, anchor='center')

    entry = tk.Entry(root, width=30)
    entry.place(relx=0.5, rely=0.5, anchor='center')

    def put_title():
        value = entry.get().strip()
        if value == "":
            messagebox.showerror('Error', 'Please enter a title')
            return

        root.title(value)
        label.destroy()
        entry.destroy()
        create_btn.destroy()
        show_add_button()

    create_btn = tk.Button(root, text='Create', command=put_title)
    create_btn.place(relx=0.5, rely=0.6, anchor='center')


def show_add_button():
    global add_btn
    if add_btn:
        add_btn.destroy()
    add_btn = tk.Button(root, text='Add', command=add_task_row)
    add_btn.place(relx=0.5, rely=0.15, anchor='center')


def hide_existing_tasks():
    for row in task_rows:
        row.grid_remove()


def show_existing_tasks():
    for row in task_rows:
        row.grid()


def add_task_row():
    global tasks_frame, add_btn, editor_widgets

    if add_btn:
        add_btn.destroy()
        add_btn = None
    hide_existing_tasks()

    if tasks_frame is None:
        init_tasks_frame()

    entry = tk.Entry(tasks_frame, width=30)
    entry.grid(row=len(task_rows), column=0, padx=6, pady=6, sticky="w")

    def finalize_task():
        global editor_widgets
        text = entry.get().strip()
        if not text:
            messagebox.showwarning("Empty task", "Please enter a task before pressing Done.")
            return

        for w in editor_widgets:
            w.destroy()
        editor_widgets = []

        row_frame = tk.Frame(tasks_frame)
        lbl = tk.Label(row_frame, text=text, anchor="w")
        lbl.grid(row=0, column=0, padx=6, pady=6, sticky="w")

        var = tk.BooleanVar(value=False)

        def toggle_status():
            # по желание: зачеркване при Completed
            lbl.config(font=("", 10, "overstrike" if var.get() else "normal"))

        chk = tk.Checkbutton(row_frame, text="In Progress", variable=var,
                             command=lambda: (chk.config(text="Completed" if var.get() else "In Progress"),
                                              toggle_status()))
        chk.grid(row=0, column=1, padx=6, pady=6)

        row_frame.grid(row=len(task_rows), column=0, columnspan=2, sticky="w")
        task_rows.append(row_frame)
        show_existing_tasks()
        show_add_button()

    done_btn = tk.Button(tasks_frame, text="Done", command=finalize_task)
    done_btn.grid(row=len(task_rows), column=1, padx=6, pady=6)

    editor_widgets = [entry, done_btn]


def init_tasks_frame():
    global tasks_frame
    tasks_frame = tk.Frame(root)
    tasks_frame.place(relx=0.5, rely=0.55, anchor='center')


root = tk.Tk()
root.geometry('500x420')
root.title("To-Do App")
start_btn = tk.Button(root, text='Create to-do List', command=create_title)
start_btn.place(relx=0.5, rely=0.5, anchor="center")
root.mainloop()
