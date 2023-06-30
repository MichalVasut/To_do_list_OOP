import customtkinter
import tkinter


class MyButton(customtkinter.CTkButton):
    """
    Univerzální tlačítko. Vyžaduje zadání těchto argumentů:
    - s_row: pořadí řádku
    - s_column: pořadí sloupce 
    """
    def __init__(self, listbox, input_area, s_row, s_column, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.listbox = listbox
        self.input_area = input_area
        self.configure(width=80,
                       fg_color="#088",
                       hover_color="#066",
                       corner_radius=6,
                       font=("Yu Gothic", 14))
        self.grid(padx=2.5, pady=10,
                  ipadx=4, ipady=0,
                  row=s_row, column=s_column,
                  sticky="w"+"e")
        
        
    def fu_add_button(self):
        """
        Funkce přidává funkcionalitu tlačítku "PŘIDAT" (add_button).
        Konkrétně přidá zapsanou položku do seznamu úkolů.
        """
        ukol = self.input_area.get()
        if ukol != "":
            self.listbox.insert(0, ukol)
            self.input_area.delete("0", "end")
        else:
            print("Nelze uložit prázdnou položku.")


    def fu_delete_item(self):
        """
        Funkce přidává funkcionalitu tlačítku "SMAZAT POLOŽKU" (delete_item).
        Konrkétně vymaže položku, která je v seznamu úkolů označena.
        """
        self.listbox.delete(tkinter.ANCHOR)

    def fu_delete_list(self):
        """
        Funkce přidává funkcionalitu tlačítku "SMAZAT SEZNAM" (delete_list).
        Konrkétně vymaže celý obsah seznamu úkolů.
        """
        self.listbox.delete(0, tkinter.END)


    def fu_save_button(self):
        """
        Funkce přidává funkcionalitu tlačítku "ULOŽIT" (save_button).
        Konkrétně ukládá seznam úkolů do souboru items_list.txt.
        """
        with open("items_list.txt", mode="w", encoding="utf-8") as file:
            items_list = self.listbox.get(0, tkinter.END)
            for item in items_list:
                file.writelines(item + "\n")

