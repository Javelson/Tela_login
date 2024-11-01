import flet as ft
from controls.controls import Login  # Supondo que Login está definido em controls.py

# Função para converter RGB em hexadecimal
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

def main(page: ft.Page):
    page.title = 'Login'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = ft.padding.all(0)
    page.bgcolor = rgb_to_hex([221, 221, 221])  # Usando a função rgb_to_hex

    row = ft.Row(
        controls=[
            Login(page=page)
        ],
        alignment= ft.MainAxisAlignment.CENTER
    )
    page.add(row)

if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
 

