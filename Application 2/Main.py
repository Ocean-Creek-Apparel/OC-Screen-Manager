from model.screen import Screen
from controller.controller import Controller
import sqlite3
import json

def main():
    """
    The main application loop.
    """
    controller = Controller()
    controller.update_db_path(r'C:\Users\cugos\OneDrive\Documents\GitHub\OC-Screen-Manager\Application 2\database\Screen_Database.db')

    for screen in controller.screens:
        print(screen.design)


if __name__ == "__main__":
    main()