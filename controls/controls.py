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
                    size=14,
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
            border_width=2,
            prefix_icon=ft.icons.PERSON,
            autofocus=True
        ),
        ft.FloatingActionButton(
            text='Conecte-se',
            foreground_color= ft.colors.WHITE,
            bgcolor= rgb_to_hex([99, 182, 245]),
            width=self.width,
            height=45,
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
                     on_click= self.register_event,
                )
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            spacing=4 
        )
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    def register_event(self, e: ft.ControlEvent):
        e.page.controls.clear()
        e.page.add(Registrar(page=e.page))

class Registrar(ft.Container):
    def __init__(self, 
                 page: ft.Page
    ):
        super().__init__()
        self.ph = FilePicker(self)
        page.overlay.append(self.ph)
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
                    value='Criar Conta!',
                     color= ft.colors.with_opacity(0.6, 'black'),
                      size=22,
                     weight='bold'
                 ),
                 ft.Text(
                    value='Descubra as melhores novidades',
                    color= ft.colors.with_opacity(0.4, 'black'),
                    size=16,
                    text_align= ft.TextAlign.CENTER
                )
             ],
            spacing=0,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER
        ),
        image_pic := ft.Container(
            width=90,
            height=90,
            border_radius=90,
            image = ft.DecorationImage(
                src=None,
                fit= ft.ImageFit.COVER
            ),
            bgcolor= ft.colors.with_opacity(0.68, 'blue'),
            content= ft.Icon(
                name = ft.icons.PERSON,
                color =rgb_to_hex([58, 145, 235]),
                size=80
            )
            
        ),
        ft.Column(
            controls=[
                 ft.TextField(
            hint_text='Email',
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
            border_width=2,
            prefix_icon= ft.icons.EMAIL,
            autofocus=True
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
            border_width=2,
            prefix_icon= ft.icons.PERSON
        ),
        ft.TextField(
            hint_text='Senha',
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
            border_width=2,
            password=True,
            can_reveal_password=True,
            prefix_icon= ft.icons.KEY
        ),
         ft.TextField(
            hint_text='Confirmar Senha',
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
            border_width=2,
            password=True,
            can_reveal_password=True,
            prefix_icon= ft.icons.KEY
        ),

            ],
            spacing=5
        ),
        
        ft.FloatingActionButton(
            text='Registar ',
            foreground_color= ft.colors.WHITE,
            bgcolor= rgb_to_hex([99, 182, 245]),
            width=self.width,
            height=45,
            elevation=0
        ),
        ft.Row(
            controls=[
                ft.Text(
                    value='Já tenho uma conta',
                    size=12,
                

                ),
                ft.Container(
                    content=ft.Text(
                        value='Entrar',
                        color= rgb_to_hex([225, 110, 117])
                    ),
                     on_click= self.login_event,
                )
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            spacing=4 
        )
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER   
        )
        self.image_pic = image_pic
        
    def login_event(self, e: ft.ControlEvent):
        e.page.controls.clear()
        e.page.add(Login(page=e.page))

class FilePicker(ft.FilePicker):
    def __init__(
        self,
        control: Registrar
    ):
      super().__init__()
      self.on_result = self.file_piker_result
      self.control = control

    def file_piker_result(self, e: ft.FilePickerResultEvent):
        image_path: list[str] = []
        if e.files:
            for file in e.files:
                image_path.append(file.name)  
            self.control.image_pic.image_src = image_path[-1]
            self.control.image_pic.content = None


        e.page.update()