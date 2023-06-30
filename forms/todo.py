from customtkinter import CTk, CTkButton, CTkEntry, CTkFrame, CTkFont
from tkinter import Listbox

class TODOApp(CTk):
    # vytvoření formuláře

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Seznam úkolů")
        self.geometry("600x500")
        self.font=CTkFont(family="Arial", size=16)

        self.columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=0)

        self.create_input_frame()

        self.todo_list = Listbox(self, font=self.font)
        self.todo_list.grid(row=1, column=0, sticky="nswe", padx=5)

        self.create_buttons_frame()

    def create_input_frame(self):
        frame = CTkFrame(self)
        frame.grid(sticky="we", padx=5, pady=5)

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=0)

        self.todo_input = CTkEntry(frame, font=self.font)
        self.todo_input.grid(row=0, column=0, sticky="we")
        
        add_btn = CTkButton(frame, text="Přidat", command=self.add_todo)
        add_btn.grid(row=0, column=1)

    def create_buttons_frame(self):
        frame = CTkFrame(self)
        frame.grid(row=2, sticky="we", padx=5, pady=5)

        frame.grid_columnconfigure(0, weight=0)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=0)
        frame.grid_columnconfigure(2, weight=0)

        remove_btn = CTkButton(frame, text="Odebrat položku", command=self.remove_todo)
        remove_btn.grid(row=0, column=0)

        clear_btn = CTkButton(frame, text="Smazat seznam", command=self.clear_todos)
        clear_btn.grid(row=0, column=2, padx=5)

        save_btn = CTkButton(frame, text="Uložit seznam", command=self.save_todos)
        save_btn.grid(row=0, column=3)

    # události tlačítek

    def add_todo(self):
        value = self.todo_input.get()

        if value:
            self.todo_list.insert(self.todo_list.size(), value)
            self.todo_input.delete(0, len(self.todo_input.get()))

    def remove_todo(self):
        self.todo_list.delete(self.todo_list.curselection())

    def clear_todos(self):
        self.todo_list.delete(0, self.todo_list.size())

    def save_todos(self):
        pass



        

        

        