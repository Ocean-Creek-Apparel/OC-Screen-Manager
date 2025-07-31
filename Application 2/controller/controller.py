import sqlite3
from model.screen import Screen
from model.location import Location

class Controller:
    """
    This class coordinates the models and views to perform
    their intended tasks.

    Attributes:
        connection (sqlite3.Connection): the sqlite3 db connection
        screens (List[Screens]): a list of screens in the database
    """

    def __init__(self, db_path: str):
        self.connection = sqlite3.connect(db_path)
        self.update_screen_list()

    def update_screen_list(self):
        """
        Reads all screens from database and assigns that list to self.screens
        """
        self.screens = Screen.read_all(self.connection)

    def update_db_path(self, new_path: str):
        self.connection = sqlite3.connect(new_path)

    def add_screen(self, screen: Screen):
        """
        Add or update the provided screen's data to the db.
        
        Arguments:
            screen (Screen): the screen to update/add.
        """
        success = screen.add_to_db(self.connection)
        if success:
            self.update_screen_list()

    def delete_screen(self, screen):
        success = screen.delete_from_db(self.connection)
        if success:
            self.update_screen_list()

    
