import flet as ft

def main(page: ft.Page):
    page.title = "my first app"
    page.theme_mode = ft.ThemeMode.DARK
    
    greeting_text = ft.Text("Hello world")
    name = ft.TextField(label="Enter your name: ")
    def on_button_click(_):
        if name.value:
            greeting_text.value = f"Hello {name.value}"
            name.value = ""
        else:
            greeting_text.value = "Please Enter ur name"

        page.update()


    button= ft.ElevatedButton("SEND",icon=ft.Icons.SEND,on_click=on_button_click)

    
    page.add(name,button,greeting_text)

ft.app(target=main)