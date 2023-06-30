import customtkinter

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