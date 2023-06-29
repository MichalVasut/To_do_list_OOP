
import objects
from tkinter import ANCHOR, END, messagebox


# FUNKCE
def read_items_list():
    """
    Funkce přečte uložený seznam úkolů a zobrazí ho. Pokud 
    soubor nebyl nalezen, bude vytvořen při ukládání seznamu.

    Spouští se při spuštění programu.
    """
    try:
        with open("items_list.txt", mode="r", encoding="utf-8") as file:
            for item in file:
                listbox.insert("end", item.strip())
    except:
        print("Soubor nenalezen. Bude vytvořen při prvním uložení seznamu.")

def fu_add_button():
    """
    Funkce přidává funkcionalitu tlačítku "PŘIDAT" (add_button).
    Konkrétně přidá zapsanou položku do seznamu úkolů.
    """
    ukol = input_area.get()
    if ukol != "":
        listbox.insert(0, ukol)
        input_area.delete("0", "end")
    else:
        print("Nelze uložit prázdnou položku.")


def fu_delete_item():
    """
    Funkce přidává funkcionalitu tlačítku "SMAZAT POLOŽKU" (delete_item).
    Konrkétně vymaže položku, která je v seznamu úkolů označena.
    """
    listbox.delete(ANCHOR)

def fu_delete_list():
    """
    Funkce přidává funkcionalitu tlačítku "SMAZAT SEZNAM" (delete_list).
    Konrkétně vymaže celý obsah seznamu úkolů.
    """
    listbox.delete(0, END)


def fu_save_button():
    """
    Funkce přidává funkcionalitu tlačítku "ULOŽIT" (save_button).
    Konkrétně ukládá seznam úkolů do souboru items_list.txt.
    """
    with open("items_list.txt", mode="w", encoding="utf-8") as file:
        items_list = listbox.get(0, END)
        for item in items_list:
            file.writelines(item + "\n")

def save_control():
    """
    Funkce kontroluje, jestli je obsah seznamu úkolů stejný, 
    jako seznam uložený v items_list.txt. Spouští se ve chvíli, 
    kdy chce uživatel seznam zavřít.
    
    RETURN: True - pokud je seznam stejný
            False - pokud se seznamy liší
    """
    listbox_content = listbox.get(0, END)

    file_content = []
    with open("items_list.txt", mode="r", encoding="utf-8") as file:
        for item in file:
            file_content.append(item.strip())
    file_content = tuple(file_content)

    if listbox_content == file_content:
        return True
    else:
        return False

def closing():
    """
    Fukce se spouští při pokusu o zavření okna. Pomocí funkce
    save_control() zkontroluje, zdali byly změny v seznamu
    uloženy a pokud ne, upozorní na to uživatele.
    """
    if save_control():
        window.destroy()
    else:
        answer = messagebox.askyesno("UPOZORNĚNÍ",
                                     "Obsah není uložen. "
                                     "Opravdu chcete seznam zavřít?")
        if answer:
            window.destroy()



# HLAVNÍ OKNO
window = objects.MainWindow("seznam úkolů")
window.protocol("WM_DELETE_WINDOW", closing)


# FRAME PRO VSTUP UŽIVATELE
input_frame = objects.MyFrame(master=window, s_pady=(5, 0))
add_button = objects.MyButton(master=input_frame,
                              text="PŘIDAT",
                              s_row=0, s_column=2,
                              command=fu_add_button)
input_area = objects.MyEntry(master=input_frame,
                             s_row=0, s_column=1)

# FRAME SEZNAMU
list_frame = objects.MyFrame(master=window, s_pady=(5,0))
listbox = objects.MyListBox(master=list_frame)


# FRAME FUNKČNÍCH TLAČÍTEK
buttons_frame = objects.MyFrame(master=window, s_pady=(0,5))
delete_item = objects.MyButton(master=buttons_frame,
                               text="SMAZAT POLOŽKU",
                               s_row=0, s_column=0,
                               command=fu_delete_item)
delete_list = objects.MyButton(master=buttons_frame,
                               text="SMAZAT SEZNAM",
                               s_row=0, s_column=1,
                               command=fu_delete_list)
save_button = objects.MyButton(master=buttons_frame,
                               text="ULOŽIT",
                               s_row=0, s_column=2,
                               command=fu_save_button)

# HLAVNÍ CYKLUS
read_items_list()
window.mainloop()