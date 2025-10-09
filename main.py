import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "my first app"
    page.theme_mode = ft.ThemeMode.DARK
    now = datetime.now()

    greeting_text = ft.Text("Hello world",size=25)
    name_input = ft.TextField(label="Enter your name: ")
 
    def on_button_click(_):
        if name_input.value:
            if now.hour >= 6 and now.hour < 12:
                greeting_text.value = f"Good morning {name_input.value}"
            
            elif now.hour >= 12 and now.hour < 18:
                greeting_text.value = f"Good afternoon {name_input.value}"
            
            elif now.hour >= 18 and now.hour < 24:
                greeting_text.value = f"Good evening {name_input.value}"
            
            elif now.hour >= 0 and now.hour < 6:
                greeting_text.value = f"Good night {name_input.value}"
            
            else:
                greeting_text.value = "Time is not defined"

            name_input.value = ""
            
        else:
            greeting_text.value = "Please Enter ur name"

        page.update()

    def button_change_theme(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT

        else:
            page.theme_mode = ft.ThemeMode.DARK

        page.update()

    button= ft.ElevatedButton("SEND",icon=ft.Icons.SEND,on_click=on_button_click)
    button_for_theme = ft.ElevatedButton("CHANGE THEME",ft.Icons.BRIGHTNESS_7, on_click=button_change_theme)

    page.add(name_input,button,greeting_text,button_for_theme)

ft.app(target=main)