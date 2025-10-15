import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "my first app"
    page.theme_mode = ft.ThemeMode.DARK
    now = datetime.now()

    greeting_text = ft.Text("Hello world",size=25)
    counter_theme_text = ft.Text("",size=18)
    counter = 0

    greeting_history = []
    history_text = ft.Text(f"Story of greetings: \n",size=25)
 
    def on_button_click(_):
        timestamp = datetime.now().strftime("%H:%M:%S")
        if name_input.value and len(name_input.value) <= 12:
            greeting_history.append(
                ft.TextSpan(text=f"{timestamp} ",style=ft.TextStyle(color=ft.Colors.RED)))
            greeting_history.append(
                ft.TextSpan(text=f"{name_input.value}\n",style=ft.TextStyle(color=ft.Colors.BLUE,
                                                         weight=ft.FontWeight.BOLD)))
            
            history_text.spans = greeting_history

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
            
        else:
            if not name_input.value:
               greeting_text.value = "Please Enter ur name"
            if len(name_input.value) > 12:
               greeting_text.value = "You are allowed to print maximum 12 letters"
 
        name_input.value = ""
        page.update()
            
    def button_change_theme(_):
        if page.theme_mode == ft.ThemeMode.DARK:
           page.theme_mode = ft.ThemeMode.LIGHT
          
        else:
            page.theme_mode = ft.ThemeMode.DARK
            
        nonlocal counter
        counter += 1
        counter_theme_text.value = f"Theme was changed {counter} times"
        page.update()

    def clear_button(_):
        greeting_history.clear()
        history_text.value = "Story of greetings: \n"
        page.update()

    name_input = ft.TextField(label="Enter your name: ",on_submit=on_button_click)
    button_for_theme = ft.ElevatedButton("CHANGE THEME",ft.Icons.BRIGHTNESS_7,height=85,width=105,on_click=button_change_theme)
    button_clear = ft.IconButton(icon=ft.Icons.DELETE,on_click=clear_button,height=85,width=105)

    theme_button = ft.Row([button_for_theme], alignment = ft.MainAxisAlignment.CENTER)
    theme_text = ft.Row([counter_theme_text], alignment = ft.MainAxisAlignment.CENTER)
    story_greeting_text = ft.Row([history_text], alignment = ft.MainAxisAlignment.END)
    text_clear = ft.Row([button_clear], alignment=ft.MainAxisAlignment.START)
    
    page.add(name_input,
             greeting_text,
             theme_button,
             theme_text,
             text_clear,
             story_greeting_text)

ft.app(target=main)