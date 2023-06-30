import window_object
import frame_object
import entry_object
import listbox_object
import button_object

# HLAVNÍ OKNO
window = window_object.MainWindow(listbox=listbox, s_title="seznam úkolů")

# FRAME PRO VSTUP UŽIVATELE
input_frame = frame_object.MyFrame(master=window, s_pady=(5, 0))
input_area = entry_object.MyEntry(master=input_frame,
                             s_row=0, s_column=1)
add_button = button_object.MyButton(listbox=listbox,
                                    input_area=input_area,
                                    master=input_frame,
                                    text="PŘIDAT",
                                    s_row=0, s_column=2)
add_button.configure(command=add_button.fu_add_button)


# FRAME SEZNAMU
list_frame = frame_object.MyFrame(master=window, s_pady=(5,0))
listbox = listbox_object.MyListBox(master=list_frame)
listbox.read_items_list()


# FRAME FUNKČNÍCH TLAČÍTEK
buttons_frame = frame_object.MyFrame(master=window, s_pady=(0,5))
delete_item = button_object.MyButton(listbox=listbox,
                                    input_area=input_area,
                                    master=buttons_frame,
                                    text="SMAZAT POLOŽKU",
                                    s_row=0, s_column=0)
delete_item.configure(command=delete_item.fu_delete_item)

delete_list = button_object.MyButton(listbox=listbox,
                                    input_area=input_area,
                                    master=buttons_frame,
                                    text="SMAZAT SEZNAM",
                                    s_row=0, s_column=1)
delete_list.configure(command=delete_list.fu_delete_list)

save_button = button_object.MyButton(listbox=listbox,
                                    input_area=input_area,
                                    master=buttons_frame,
                                    text="ULOŽIT",
                                    s_row=0, s_column=2)
save_button.configure(command=save_button.fu_save_button)

# HLAVNÍ CYKLUS
window.mainloop()