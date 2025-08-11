import sqlite3
import sys
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
        locations (Dict[int, Location]): a list of locations in the database    
        observers (list[Any]): a list of observers to be notified when data is changed
    """

    def __init__(self):
        """
        Initializes a new controller. 
        """
        # Determine config path (handles PyInstaller frozen executable)
        if getattr(sys, 'frozen', False):
            base_dir = Path(sys.executable).parent
        else:
            base_dir = Path(__file__).parent.parent
        config_dir = base_dir / 'config'
        config_dir.mkdir(parents=True, exist_ok=True)
        self.config_path = config_dir / 'settings.json'
        if not self.config_path.exists():
            # create stub so json.load won't fail later
            self.config_path.write_text('{}')

        config = self.__load_config()
        db_path = config["db_path"]

        self.connection = sqlite3.connect(db_path)
        self.screens = []
        self.observers = []
        self.locations = dict()

        self.update_screens_and_locations()

    def notify_observers(self):
        """
        Executes the data_updated() function for all observers.
        """
        for observer in self.observers:
            observer.data_updated()

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

    def update_db_path(self, new_path: str):
        if (self.connection):
            self.connection.close()

        self.connection = sqlite3.connect(new_path)

        config = self.__load_config()
        config["db_path"] = new_path
        self.__save_config(config)

        self.update_screen_list()

    def update_screen_list(self):
        """
        Reads all screens from database and assigns that list to self.screens
        """
        self.screens = Screen.read_all(self.connection)
        self.notify_observers()

    def add_screen(self, screen: Screen):
        """
        Add or update the provided screen's data to the db.
        
        Arguments:
            screen (Screen): the screen to update/add.
        """
        screen.add_to_db(self.connection)
        self.update_screen_list()
        self.notify_observers()

    def delete_screen(self, screen: Screen):
        """
        Delete the passed screen.

        Arguments:
            screen (Screen): the screen to delete
        """
        screen.delete_from_db(self.connection)
        self.update_screen_list()
        self.notify_observers()

    def update_location_dict(self):
        """
        Reads all locations from the database and assigns to self.locations
        """
        locations = Location.read_all(self.connection)
        self.locations = dict(sorted(locations.items(), key=lambda item: item[1].description))
        self.notify_observers()

    def delete_location(self, location: Location):
        """
        Delete the location from the database.

        Arguments:
            location (Location): the location to delete
        """
        location.delete_from_db(self.connection)
        self.update_location_dict()
        self.notify_observers()

    def add_location(self, location: Location):
        """
        Add or update the provided location.
        
        Arguments:
            location (Location): the location to add/update
        """
        location.add_to_db(self.connection)
        self.update_location_dict()
        self.notify_observers()


    def update_screens_and_locations(self):
        """
        Runs both update_screen_list() and update_location_dict().
        Critically, locations are updated before screens.
        """
        self.update_location_dict()
        self.update_screen_list()
        self.notify_observers()
    
    
