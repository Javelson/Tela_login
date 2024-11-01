import flet as ft

# Incio

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

class Login(ft.Container):
    def __init__(self, 
                 page: ft.Page
    ):
        super().__init__()
        self.width = page.width * 1/4
        self.bgcolor = rgb_to_hex([244, 244,244])
        self.border_radius = 8
        self.border = ft.border.all(
            width=8,
            color= ft.colors.WHITE
        )
        self.padding = ft.padding.all(20)
        self.alignment = ft.alignment.center
        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls= [
                     ft.Text(
                    value='Bem vindo!',
                     color= ft.colors.with_opacity(0.6, 'black'),
                      size=22,
                     weight='bold'
                 ),
                 ft.Text(
                    value='Descubra mais \n Conectando-se a nós',
                    color= ft.colors.with_opacity(0.4, 'black'),
                    size=16,
                    text_align= ft.TextAlign.CENTER
                )
             ],
            spacing=0,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        ),
        ft.Container(
            width=90,
            height=90,
            border_radius=90,
            bgcolor= ft.colors.with_opacity(0.68, 'blue'),
            content= ft.Icon(
                name = ft.icons.PERSON,
                color =rgb_to_hex([58, 145, 235]),
                size=80
            )
            
        ),
        ft.TextField(
            hint_text='Username',
            hint_style=ft.TextStyle(
                size=13,
                color=ft.colors.with_opacity(0.4, 'Black'),
                weight='bold'
            ),
            text_style=ft.TextStyle(
                size=13,
                color=ft.colors.with_opacity(0.8, 'Black'),
                weight='bold'
            ),
            bgcolor= ft.colors.with_opacity(0.6, 'white'),
            border_radius=8,
            border_color= ft.colors.WHITE,
            border_width=2
        ),
        ft.FloatingActionButton(
            text='Conecte-se',
            foreground_color= ft.colors.WHITE,
            bgcolor= rgb_to_hex([99, 182, 245]),
            width=self.width,
            height=50,
            elevation=0
        ),
        ft.Row(
            controls=[
                ft.Text(
                    value='Não tenho uma conta!',
                    size=12,
                

                ),
                ft.Container(
                    content=ft.Text(
                        value='Criar uma conta',
                        color= rgb_to_hex([225, 110, 117])
                    ),
                     on_click=lambda _: print('cliquei no botão'),
                )
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            spacing=4 
        )
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER

           
        )
        