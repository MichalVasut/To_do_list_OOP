import customtkinter

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
                       font=("Yu Gothic", 14))
        self.grid(padx=2.5, pady=10,
                  row=s_row, column=s_column,
                  sticky="w"+"e")
        self.focus_set()