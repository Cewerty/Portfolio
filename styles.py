import flet as ft
from typing import Optional, List, Any

def style_card(content, width=True, padding: Optional[ft.Padding] = None):
    if padding is None:
        padding = ft.Padding(16, 16, 16, 16)
    return ft.Card(
        content=ft.Container(
            content=content,
            # border_radius=4,
            # border=ft.Border(top=ft.BorderSide(1, ft.colors.GREY_500),
            #                  left=ft.BorderSide(0),
            #                  right=ft.BorderSide(0),
            #                  bottom=ft.BorderSide(1, ft.colors.GREY_500)),
            width=width,
            padding=padding,
            margin=ft.Margin(16, 16, 0, 0),
        )
    )

def style_title(text, font_size=20, color='white'):
    return ft.Text(
        text,
        style=ft.TextStyle(
            color=color,
            size=font_size,
            weight=ft.FontWeight.BOLD,
        )
    )

def style_text(text, font_size=16, color='white'):
    return ft.Text(
        text,
        style=ft.TextStyle(
            color=color,
            size=font_size,
        )
    )

def style_header(text:str, font_size=24, color='blue'):
    return ft.Text(
        text,
        style=ft.TextStyle(
            color=color,
            size=font_size,
            weight=ft.FontWeight.BOLD,
        )
    )


def create_container(title: str,
                     elements: List[Any],
                     width=True,
                     height=True,
                     spacing: Optional[ft.Padding] = None,):
    if spacing is None:
        padding = ft.Padding(16, 16, 16, 16)
    return ft.Container(
        content=ft.Column(
            [
                ft.Column([style_header(title)], alignment=ft.MainAxisAlignment.START),
                ft.Divider(height=1, color=ft.colors.GREY_600, thickness=5, opacity=0.25),
                ft.Column(elements, alignment=ft.MainAxisAlignment.CENTER),
            ]
            
            ),
        width=width,
        height=height,
        padding=padding,
        # alignment=ft.Alignment(x=0, y=0),
        
    )   


def contact_list_item(phone: str,
                      email: str,
                      telegram: str,
                      github: str):
    return ft.ListTile(
        subtitle=ft.Column(
            [
                ft.Row(
                    [
                        ft.Icon(ft.icons.PHONE),
                        style_text(f"Phone: {phone}"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Row(
                    [
                        ft.Icon(ft.icons.EMAIL),
                        style_text(f"Email: {email}"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Row(
                    [
                        ft.Icon(ft.icons.MESSAGE),
                        style_text(f"Telegram: {telegram}"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
                ft.Row(
                    [
                        ft.Icon(ft.icons.CODE),
                        style_text(f"GitHub: {github}"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                ),
            ]
        ),
    )
    
    
def project_card(project: dict):
    return style_card(
        ft.Column(
            [
                style_header(project['name']),
                style_text(project['description']),
                ft.Row(
                    [
                        ft.TextButton("View on GitHub", url=project['github']),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                ),
            ]
        )
    )
    

def skills_card(project: dict):
    return style_card(
        ft.Column(
            [
                ft.Row([style_header(project['name'])], alignment=ft.MainAxisAlignment.CENTER),
                style_text(project['description']),
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )
    

# def profile_card(profile: dict):
#     return style_card(
#         ft.Column(
#             [
#                 ft.Row([
#                     ft.Icon(ft.icons.PHONE),
#                     f"{style_title('Phone number')}: {style_text(profile['phone'])}"],
#                     alignment=ft.MainAxisAlignment.CENTER),
#                 f"{style_title("Email")}: {style_text(profile['email'])}",
#                 f'{style_title("Telegram")}: {style_text(profile["Telegram"])}',
#                 f'{style_title("Github")}: {style_text(profile["github"])}',
#             ], alignment=ft.MainAxisAlignment.CENTER
#         )
#     )