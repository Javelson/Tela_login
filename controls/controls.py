import flet as ft
from flet_toast import flet_toast
from flet import FilePicker  # Importando corretamente

# Função auxiliar para converter RGB para HEX
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

class LoginUsername(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.width = page.width * 1/4
        self.bgcolor = rgb_to_hex([244, 244, 244])
        self.border_radius = 8
        self.border = ft.border.all(
            width=8,
            color=ft.colors.WHITE
        )
        self.padding = ft.padding.all(20)
        self.alignment = ft.alignment.center
        self.ph = FilePicker(self)  # Adicionando FilePicker aqui
        page.overlay.append(self.ph)
        
        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            value='Bem vindo!',
                            color=ft.colors.with_opacity(0.6, 'black'),
                            size=22,
                            weight='bold'
                        ),
                        ft.Text(
                            value='Descubra mais \n Conectando-se a nós',
                            color=ft.colors.with_opacity(0.4, 'black'),
                            size=14,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Container(
                    width=90,
                    height=90,
                    border_radius=90,
                    bgcolor=ft.colors.with_opacity(0.68, 'blue'),
                    content=ft.Icon(
                        name=ft.icons.PERSON,
                        color=rgb_to_hex([58, 145, 235]),
                        size=80
                    ),
                    on_click=lambda _: self.ph.pick_files(  # Evento para escolher a imagem
                        dialog_title='Escolher imagem de perfil',
                        file_type=ft.FilePickerFileType.IMAGE
                    )
                ),
                ft.TextField(
                    hint_text='Username',
                    hint_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.4, 'black'),
                        weight='bold'
                    ),
                    text_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.8, 'black'),
                        weight='bold'
                    ),
                    bgcolor=ft.colors.with_opacity(0.6, 'white'),
                    border_radius=8,
                    border_color=ft.colors.WHITE,
                    border_width=2,
                    prefix_icon=ft.icons.PERSON,
                    autofocus=True
                ),
                ft.FloatingActionButton(
                    text='Conecte-se',
                    foreground_color=ft.colors.WHITE,
                    bgcolor=rgb_to_hex([99, 182, 245]),
                    width=self.width,
                    height=45,
                    elevation=0,
                    on_click=self.get_password
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
                                color=rgb_to_hex([225, 110, 117])
                            ),
                            on_click=self.register_event,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=4
                )
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def get_password(self, e: ft.ControlEvent):
        username = e.control.parent.controls[2].value

        if username:
            e.page.controls.clear()
            e.page.add(LoginPassword(page=e.page, username=username))
        else:
            flet_toast.warning(
                page=e.page,
                message='Usuario não existe',
                position=flet_toast.Position.TOP_RIGHT
            )

    def register_event(self, e: ft.ControlEvent):
        e.page.controls.clear()
        e.page.add(Registrar(page=e.page))


# Modificando a classe FilePicker
class FilePicker(ft.FilePicker):
    def __init__(
        self,
        control: LoginUsername  # Passando o controle de LoginUsername aqui
    ):
        super().__init__()
        self.on_result = self.file_picker_result
        self.control = control

    def file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            # Pegando o arquivo selecionado
            file_path = e.files[0].name
            print(f'Imagem escolhida: {file_path}')
            
            # Mudando a imagem de perfil
            self.control.content.controls[1].image_src = file_path
            self.control.content.controls[1].content = None

        e.page.update()


class LoginPassword(ft.Container):
    def __init__(self, page: ft.Page, username: str):
        super().__init__()
        self.username = username
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
                        value=self.username,
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
            prefix_icon=ft.icons.KEY,
            autofocus=True,
            password=True,
            can_reveal_password=True
        ),
        ft.FloatingActionButton(
            text='Entrar ',
            foreground_color= ft.colors.WHITE,
            bgcolor= rgb_to_hex([99, 182, 245]),
            width=self.width,
            height=45,
            elevation=0
        ),
        ft.Row(
            controls=[
                ft.Text(
                    value='Esqueci minha senha!',
                    size=12,
                

                ),
                ft.Container(
                    content=ft.Text(
                        value='Recuperar',
                        color= rgb_to_hex([225, 110, 117])
                    ),
                     on_click= self.resertPassword_event,
                )
            ],
            alignment= ft.MainAxisAlignment.CENTER,
            spacing=4 
        )
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    def resertPassword_event(self, e: ft.ControlEvent):
        e.page.controls.clear()
        e.page.add(ResetPassword(page=e.page, username=self.username))

class ResetPassword(ft.Container):
    def __init__(self, 
                 page: ft.Page,
                 username: str
    ):
        super().__init__()
        self.username = username
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
                    value='Recuperar Conta',
                     color= ft.colors.with_opacity(0.6, 'black'),
                      size=22,
                     weight='bold'
                 ),
                 ft.Text(
                    value='Recupere a sua conta Agora, não fica fore das novidades',
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
            ),
            on_click=lambda _: self.ph.pick_files(
                dialog_title='image Picture',
                file_type= ft.FilePickerFileType.IMAGE
            )
        ),
        ft.Column(
            controls=[
                ft.TextField(
                    value=self.username,
            hint_text='Username',
            hint_style=ft.TextStyle(
                size=13,
                color=ft.colors.with_opacity(0.4, 'Black'),
                weight='bold'
            ),
            text_style=ft.TextStyle(
                size=13,
                color=ft.colors.with_opacity(0.4, 'Black'),
                weight='bold'
            ),
            bgcolor= ft.colors.with_opacity(0.4, 'white'),
            border_radius=8,
            border_color= ft.colors.WHITE,
            border_width=2,
            prefix_icon= ft.icons.PERSON,
            disabled=True
        ),
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
         
      
            ],
            spacing=5
        ),
        
        ft.FloatingActionButton(
            text='Recuperar  ',
            foreground_color= ft.colors.WHITE,
            bgcolor= rgb_to_hex([99, 182, 245]),
            width=self.width,
            height=45,
            elevation=0,
            on_click= self.get_confrm_Code
        ),
       
        ],
        spacing=10,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER   
        )
        self.image_pic = image_pic

    def  get_confrm_Code(self, e: ft.ControlEvent):
        e.page.controls.clear()
        e.page.add(ConfirmCode(page=e.page, username=self.username, confirm_code='AA123' ))
        
class ConfirmCode(ft.Container):
    def __init__(self, 
                 page: ft.Page,
                 username : str,
                 confirm_code: str
    ):
        super().__init__()
        self.username = username
        self.confirm_code = confirm_code
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
                    value=self.username,
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
          ft.ResponsiveRow(
                     controls=[
                         ft.TextField(
                             text_align= ft.TextAlign.CENTER,
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
            autofocus=True,
            col={'xs': 2.40, 'sm': 2.40},
            data=lambda index = i: index,
            on_change= self.change_value if i < 4 else self.Confirm_code_event
            
        ) for i in range(5)
                         
                     ]
                 ),
        
        ft.FloatingActionButton(
            text='Confirmar ',
            foreground_color= ft.colors.WHITE,
            bgcolor= rgb_to_hex([99, 182, 245]),
            width=self.width,
            height=45,
            elevation=0,
            on_click= self.Confirm_code_event
        ),
       
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    def change_value(self, e: ft.ControlEvent):
        textfield: ft.TextField = e.control
        if len(textfield.value.strip())> 1:
            textfield.value= textfield.value[-1]
        if len(textfield.value.strip()) ==1 and textfield.data() < 4:
            textfield.parent.controls[textfield.data() + 1].focus()

        elif len(textfield.value.strip())==0 and textfield.data() > 0:
            textfield.parent.controls[textfield.data() - 1].focus()
       
        e.page.update()
    def Confirm_code_event(self, e: ft.ControlEvent):
        if e.control._get_control_name() == 'textfield':
            textfields: list[ft.TextField] = e.control.parent.controls
        else :
            textfields: list[ft.TextField] = e.control.parent.controls[2].controls

        values: str = ''.join([textfield.value for textfield in textfields])
        if len(values.strip()) == 5 and self.confirm_code == values:
            e.page.controls.clear()
            e.page.add(LoginUsername(page=e.page))
        else:
            for textfield in textfields:
                textfield.value = ''
            textfields[0].focus()

            flet_toast.warning(
                page=e.page,
                message= 'Dados invalidos, tente novamente',
                position=flet_toast.Position.TOP_RIGHT
        )

class Registrar(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.width = page.width * 1/4
        self.bgcolor = rgb_to_hex([244, 244, 244])
        self.border_radius = 8
        self.border = ft.border.all(
            width=8,
            color=ft.colors.WHITE
        )
        self.padding = ft.padding.all(20)
        self.alignment = ft.alignment.center

        self.ph = FilePicker(self)  # Adicionando FilePicker para o registro
        page.overlay.append(self.ph)

        self.content = ft.Column(
            controls=[
                ft.Column(
                    controls=[
                        ft.Text(
                            value='Criar uma conta',
                            color=ft.colors.with_opacity(0.6, 'black'),
                            size=22,
                            weight='bold'
                        ),
                        ft.Text(
                            value='Preencha as informações abaixo para criar sua conta.',
                            color=ft.colors.with_opacity(0.4, 'black'),
                            size=14,
                            text_align=ft.TextAlign.CENTER
                        )
                    ],
                    spacing=0,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                ft.Container(
                    width=90,
                    height=90,
                    border_radius=90,
                    bgcolor=ft.colors.with_opacity(0.68, 'blue'),
                    content=ft.Icon(
                        name=ft.icons.PERSON,
                        color=rgb_to_hex([58, 145, 235]),
                        size=80
                    ),
                    on_click=lambda _: self.ph.pick_files(  # Evento para escolher a imagem
                        dialog_title='Escolher imagem de perfil',
                        file_type=ft.FilePickerFileType.IMAGE
                    )
                ),
                ft.TextField(
                    hint_text='Nome completo',
                    hint_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.4, 'black'),
                        weight='bold'
                    ),
                    text_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.8, 'black'),
                        weight='bold'
                    ),
                    bgcolor=ft.colors.with_opacity(0.6, 'white'),
                    border_radius=8,
                    border_color=ft.colors.WHITE,
                    border_width=2,
                    prefix_icon=ft.icons.PERSON,
                ),
                ft.TextField(
                    hint_text='Email',
                    hint_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.4, 'black'),
                        weight='bold'
                    ),
                    text_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.8, 'black'),
                        weight='bold'
                    ),
                    bgcolor=ft.colors.with_opacity(0.6, 'white'),
                    border_radius=8,
                    border_color=ft.colors.WHITE,
                    border_width=2,
                    prefix_icon=ft.icons.EMAIL,
                ),
                ft.TextField(
                    hint_text='Senha',
                    hint_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.4, 'black'),
                        weight='bold'
                    ),
                    text_style=ft.TextStyle(
                        size=13,
                        color=ft.colors.with_opacity(0.8, 'black'),
                        weight='bold'
                    ),
                    bgcolor=ft.colors.with_opacity(0.6, 'white'),
                    border_radius=8,
                    border_color=ft.colors.WHITE,
                    border_width=2,
                    prefix_icon=ft.icons.LOCK,
                    password=True
                ),
                ft.FloatingActionButton(
                    text='Registrar',
                    foreground_color=ft.colors.WHITE,
                    bgcolor=rgb_to_hex([99, 182, 245]),
                    width=self.width,
                    height=45,
                    elevation=0,
                    on_click=self.register_user
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                            value='Já tenho uma conta!',
                            size=12,
                        ),
                        ft.Container(
                            content=ft.Text(
                                value='Fazer login',
                                color=rgb_to_hex([225, 110, 117])
                            ),
                            on_click=self.login_event,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=4
                )
            ],
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    def register_user(self, e: ft.ControlEvent):
        # Aqui, você captura os dados do usuário do formulário
        nome = e.control.parent.controls[2].value
        email = e.control.parent.controls[3].value
        senha = e.control.parent.controls[4].value
        
        if nome and email and senha:
            # Aqui você pode adicionar a lógica de salvar no banco de dados ou na memória
            flet_toast.success(
                page=e.page,
                message='Conta criada com sucesso!',
                position=flet_toast.Position.TOP_RIGHT
            )
            # Você pode redirecionar para a tela de login ou outra ação
            e.page.controls.clear()
            e.page.add(LoginUsername(page=e.page))
        else:
            flet_toast.warning(
                page=e.page,
                message='Preencha todos os campos!',
                position=flet_toast.Position.TOP_RIGHT
            )

    def login_event(self, e: ft.ControlEvent):
        e.page.controls.clear()
        e.page.add(LoginUsername(page=e.page))

# Mudança na classe FilePicker para lidar com a imagem na tela de registrar também
class FilePicker(ft.FilePicker):
    def __init__(
        self,
        control: Registrar  # Agora a referência é para Registrar
    ):
        super().__init__()
        self.on_result = self.file_picker_result
        self.control = control

    def file_picker_result(self, e: ft.FilePickerResultEvent):
        if e.files:
            # Pegando o arquivo selecionado
            file_path = e.files[0].name
            print(f'Imagem escolhida: {file_path}')
            
            # Mudando a imagem de perfil
            self.control.content.controls[1].image_src = file_path
            self.control.content.controls[1].content = None

        e.page.update()
