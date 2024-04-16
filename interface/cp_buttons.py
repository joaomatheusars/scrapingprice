from customtkinter import CTkFont, CTkButton
from typing import Union, Callable, Any

def buttons(master, text='', bg_color='blue', hover_color='blue', size=16, command: Union[Callable[[], Any], None] = None):
        my_font = CTkFont(size=size, weight='bold')
        button = CTkButton(master,
            text=text, fg_color=bg_color, hover_color=hover_color,  font=my_font, command=command)
        return button