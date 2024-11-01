import flet as ft
from hex2rgb import rgb2hex
from controls import Login 

def main(page: ft.Page):
    page.title = 'Login'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.page = ft.padding.all(0)
    page.bgcolor = rgb2hex([221,221,221])

    row = ft.Row(
        controls=[
            Login(page=page)
        ]
    )  
    page.add(row)
if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
 

