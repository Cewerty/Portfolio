import flet as ft
from styles import style_title, contact_list_item, create_container, project_card, skills_card

def main(page: ft.Page):
    
    page.title = "Моё портфолио"
    # page.vertical_alignment = "start"

    # Фото и имя
    profile_pic = ft.CircleAvatar(
        content=ft.Icon(ft.icons.PERSON),
        bgcolor=ft.colors.WHITE,
        radius=50,
    )
    
    name = style_title('Ilya\nTimofeev', 24, 'blue')
    
    profile = ft.Container(content=ft.Row(controls=[profile_pic, name], alignment=ft.MainAxisAlignment.SPACE_AROUND, spacing=10),
                           alignment=ft.Alignment(x=0, y=0),
                           padding=ft.Padding(10, 10, 20, 20),
                           width=True,
                           height=True)
    
    # Контакты
    contact_list = contact_list_item("+123456789", "email@example.com", "telegram", "github")
    
    contact = create_container('Контакты', [contact_list])
    # Навыки
    skills_dict = [{
        "name": 'Анализ данных',
        "description":"""
        Визуализация с помощью seaborn/matplotlib,
        Очистка данных с помощью pandas,
        Статистический анализ с помощью scipy, statsmodels, numpy.
        """},
        {
        "name": "База данных",
        "description":
        """
        Знание SQL,
        Знание PostgreSQL + asyncpg, SQLite + aiosqlite, Redis + aioredis,
        Знание SQLAlchemy + Alembic.
        """,
        },
        {
        "name": "Веб-разработка",
        "description":
        """
        Понимание веб-технологий и стандартов,
        Знание HTML + CSS + JS,
        Знание Django + DRF, Flask, FastAPI,
        Знание uvicorn, gunicorn, nginx.
        """,
        },
    ]
    
    skills_cards = [skills_card(skill) for skill in skills_dict]
    
    skills = create_container('Навыки', skills_cards)
    # Проекты    
    projects = [
        {"name": "Alchemy", "description": "Tool for chemical calculations and analysis", "github": "https://github.com/user/Alchemy"},
        {"name": "Homework Bot", "description": "Telegram bot for creating and watching homework posts.", "github": "https://github.com/user/homework_bot"},
        {"name": "Predloshka", "description": "Telegram bot for communication with comminity.", "github": "https://github.com/user/predloshka"},
    ]
    projects_cards = [project_card(project) for project in projects]
    
    about_project = create_container('Проекты', projects_cards)

    # Сборка страницы
    page.add(
        ft.Container(
        content=ft.Column(
            [profile, contact, ft.ListView([skills], spacing=10, auto_scroll=True),
             ft.ListView([about_project], spacing=10, auto_scroll=True)],
            scroll=ft.ScrollMode.AUTO,
        ),
        alignment= ft.Alignment(x=0, y=0),
        width=True,
        height=True,
        expand=True, 
    ),
    )
ft.app(target=main, view=ft.AppView.WEB_BROWSER) 
