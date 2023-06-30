import tkinter
import customtkinter


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
                       font=("Yu Gothic", 11))
        self.grid(row=0, column=0, padx=2.5, pady=5)

        scrollbar = customtkinter.CTkScrollbar(master=master, command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.configure(yscrollcommand=scrollbar.set)
    
    def read_items_list(self):
        """
        Funkce přečte uložený seznam úkolů a zobrazí ho. Pokud 
        soubor nebyl nalezen, bude vytvořen při ukládání seznamu.

        Spouští se při spuštění programu.
        """
        try:
            with open("items_list.txt", mode="r", encoding="utf-8") as file:
                for item in file:
                    self.insert("end", item.strip())
        except:
            print("Soubor nenalezen. Bude vytvořen při prvním uložení seznamu.")

