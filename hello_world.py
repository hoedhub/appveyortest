# importing the library
import flet as ft

# defininng the main function
def main(page: ft.Page):
    page.title = 'Hello World'

    tcLabel = ft.Text(value='My first flet app!', color="red")

    page.add(tcLabel)
    page.update()

# starting the app
ft.app(target= main)
