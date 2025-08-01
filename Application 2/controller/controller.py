import sqlite3
from model.screen import Screen
from model.location import Location
from pathlib import Path
import json

class Controller:
    """
    This class coordinates the models and views to perform
    their intended tasks.

    Attributes:
        config_path (Path): the path to the config (../config/settings.json on this machine)
        connection (sqlite3.Connection): the sqlite3 db connection
        screens (list[Screen]): a list of screens in the database 
        locations (list[Location]): a list of locations in the database    
    """

    def __init__(self):

        self.config_path = Path(__file__).parent.parent / "config" / "settings.json"

        config = self.__load_config()
        db_path = config["db_path"]

        self.connection = sqlite3.connect(db_path)
        self.screens = []
        self.locations = []

        self.update_screens_and_locations()

    def __load_config(self):
        """
        Loads config from the /config/settings.json file.

        Returns:
            json (dict[str, Any]): json data from config
        """
        with open(self.config_path, "r") as f:
            return json.load(f)
        
    def __save_config(self, config):
        """
        Saves config to the settings.json file.

        Arguments:
            config: the config to save
        """
        with open(self.config_path, "w") as f:
            json.dump(config, f, indent=2)

    def update_screen_list(self):
        """
        Reads all screens from database and assigns that list to self.screens
        """
        self.screens = Screen.read_all(self.connection)

    def update_location_list(self):
        """
        Reads all locations from the database and assigns to self.locations
        """
        self.locations = Location.read_all(self.connection)

    def update_db_path(self, new_path: str):
        if (self.connection):
            self.connection.close()

        self.connection = sqlite3.connect(new_path)

        config = self.__load_config()
        config["db_path"] = new_path
        self.__save_config(config)

        self.update_screen_list()


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

    def update_screens_and_locations(self):
        self.update_screen_list
        self.update_location_list
    
