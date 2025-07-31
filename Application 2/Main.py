from model.screen import Screen
import sqlite3

def main():
    """
    The main application loop.
    """
    conn = sqlite3.Connection(r'C:\Users\cugos\OneDrive\Documents\GitHub\OC-Screen-Manager\Application 2\database\Screen_Database.db')
    screens = Screen.read_all(conn)
    print("hello")
    for screen in screens:
        print(screen.design)

if __name__ == "__main__":
    main()