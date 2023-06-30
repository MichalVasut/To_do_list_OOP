import tkinter
import customtkinter


class MainWindow(customtkinter.CTk):
    """
    Univerzální okno. Vyžaduje zadání jednoho argumentu,
    a to názvu okna, který se zobrazí v horní liště.
    """
    def __init__(self, listbox, s_title):
        super().__init__()
        self.listbox = listbox
        self.resizable(False, False)
        self.title(s_title)

        self.protocol("WM_DELETE_WINDOW", self.closing)

    def save_control(self):
        """
        Funkce kontroluje, jestli je obsah seznamu úkolů stejný, 
        jako seznam uložený v items_list.txt. Spouští se ve chvíli, 
        kdy chce uživatel seznam zavřít.
        
        RETURN: True - pokud je seznam stejný
                False - pokud se seznamy liší
            """
        listbox_content = self.listbox.get(0, tkinter.END)

        file_content = []
        with open("items_list.txt", mode="r", encoding="utf-8") as file:
            for item in file:
                file_content.append(item.strip())
        file_content = tuple(file_content)

        if listbox_content == file_content:
            return True
        else:
            return False
        
    def closing(self):
        """
        Fukce se spouští při pokusu o zavření okna. Pomocí funkce
        save_control() zkontroluje, zdali byly změny v seznamu
        uloženy a pokud ne, upozorní na to uživatele.
        """
        if self.save_control():
            self.destroy()
        else:
            answer = tkinter.messagebox.askyesno("UPOZORNĚNÍ",
                                        "Obsah není uložen. "
                                        "Opravdu chcete seznam zavřít?")
            if answer:
                self.destroy()