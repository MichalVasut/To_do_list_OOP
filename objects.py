import tkinter
import customtkinter

main_font = ("Yu Gothic", 14)
box_font = ("Yu Gothic", 11)

class MainWindow(customtkinter.CTk):
    """
    Univerzální okno. Vyžaduje zadání jednoho argumentu,
    a to názvu okna, který se zobrazí v horní liště.
    """
    def __init__(self, s_title):
        super().__init__()
        self.resizable(False, False)
        self.title(s_title)
        

class MyFrame(customtkinter.CTkFrame):
    """
    Univerzální frame. Vyžaduje argument "s_pady"
    (okraj po ose "y"), pokud ale není zadán, použije
    se výchozí hodnota "0".
    """
    def __init__(self, s_pady=0, **kwargs):
        super().__init__(**kwargs)
        self.configure(width=550,
                       fg_color="#d4ddd8",
                       corner_radius=0)
        self.grid(padx=10,
                  pady=s_pady,
                  sticky="w"+"e")

class MyEntry(customtkinter.CTkEntry):
    """
    Univerzální okno pro získání vstupu uživatele.
    Vyžaduje argumenty:
    - s_row: pořadí řádku
    - s_column: pořadí sloupce 
    """
    def __init__(self, s_row, s_column, **kwargs):
        super().__init__(**kwargs)
        self.configure(width=305,
                       border_width=0,
                       corner_radius=6,
                       font=main_font)
        self.grid(padx=2.5, pady=10,
                  row=s_row, column=s_column,
                  sticky="w"+"e")
        self.focus_set()

class MyListBox(tkinter.Listbox):
    """
    Univerzální prostor pro zobrazení zadaného seznamu,
    které má na sebe napojenou také scrolovací lištu.
    Vyžaduje pouze argument "master" (umístění).
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(activestyle="underline",
                       relief="flat",
                       selectbackground="#d4ddd8",
                       width=42,
                       font=box_font)
        self.grid(row=0, column=0, padx=2.5, pady=5)

        scrollbar = customtkinter.CTkScrollbar(master=master, command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.configure(yscrollcommand=scrollbar.set)


class MyButton(customtkinter.CTkButton):
    """
    Univerzální tlačítko. Vyžaduje zadání těchto argumentů:
    - s_row: pořadí řádku
    - s_column: pořadí sloupce 
    """
    def __init__(self, s_row, s_column, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(width=80,
                       fg_color="#088",
                       hover_color="#066",
                       corner_radius=6,
                       font=main_font)
        self.grid(padx=2.5, pady=10,
                  ipadx=4, ipady=0,
                  row=s_row, column=s_column,
                  sticky="w"+"e")






        








