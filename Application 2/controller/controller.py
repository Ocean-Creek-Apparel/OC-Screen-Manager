import sqlite3

class Controller:
    """
    This class coordinates the models and views to perform
    their intended tasks.

    Attributes:
        connection (Connection): the sqlite3 db connection
    """

    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)

    def update_db_path(self, new_path):
        self.connection = sqlite3.connect(new_path)

    def delete_screen(id):
        pass

    def update_screen(id):
        pass

    def create_screen():
        pass
